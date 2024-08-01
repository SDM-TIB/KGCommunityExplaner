from SPARQLWrapper import SPARQLWrapper, JSON
import pandas as pd

sparql = SPARQLWrapper("https://labs.tib.eu/sdm/LungCancer/sparql")
entity_type = 'http://example.org/lungCancer/entity/Patient'


def adding_prefix(df_g):
    df_g.replace('http://www.w3.org/1999/02/22-rdf-syntax-ns#', '', regex=True, inplace=True)
    df_g.replace('http://example.org/lungCancer/entity/', '', regex=True, inplace=True)
    return df_g


def retrieve_entity(entity_type, sparql):
    q_entity = """
    prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    SELECT DISTINCT ?ego_entity
    WHERE {
      ?ego_entity a <"""+entity_type+"""> .

    }
    """
    sparql.setQuery(q_entity)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    return results

def extract_ego_network(entity, sparql):
    #     === Query to retrive the ego network
    q_ego_network = """
    SELECT DISTINCT ?subject ?predicate ?object
    WHERE {
      {
        <""" + entity + """> ?predicate ?object .
        BIND(<""" + entity + """> AS ?subject)
      }
      OPTIONAL {
        ?subject ?predicate <""" + entity + """> .
        BIND(<""" + entity + """> AS ?object)
      }
    }
    """
    sparql.setQuery(q_ego_network)
    sparql.setReturnFormat(JSON)
    triples = sparql.query().convert()
    return triples


def composite_embedding(entity_type, sparql):
    aggregate_vector = dict()
    # === Retrieve entities of type T ===
    results = retrieve_entity(entity_type, sparql)
    df_ego_network = pd.DataFrame()
    for r in results['results']['bindings']:
        ego_network = []
        entity = r['ego_entity']['value']
        # === Extract ego network of 'entity' ===
        triples = extract_ego_network(entity, sparql)
        for p in triples['results']['bindings']:
            row = {'subject': p['subject']['value'], 'predicate': p['predicate']['value'],
                   'object': p['object']['value']}
            ego_network.append(row)

        # == Data frame of ego network. Output: four columns, the last one is the ego entity.
        ego_network = pd.DataFrame.from_dict(ego_network)
        ego_network['ego_entity'] = entity
        ego_network = adding_prefix(ego_network)

        # === Function to aggregate vectors. Input:ego_network. Output: Dictionary with the following structure: aggregate = {'entity_1': [1,3,4]}

        aggregate_vector.update(aggregate)

    aggregate_vector = pd.DataFrame.from_dict(aggregate_vector, orient='index')

    # Reset the index to make the entity names a column
    aggregate_vector = aggregate_vector.reset_index()
    aggregate_vector.rename(columns={"index": "Entity"}, inplace=True)
    return aggregate_vector

