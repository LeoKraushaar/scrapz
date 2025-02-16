from pymongo import MongoClient
from dotenv import load_dotenv
from pprint import pprint
import os

class MongoManager:

    def __init__(self, db_name:str):
        load_dotenv()
        self.client = MongoClient(os.getenv('MONGO_URI'))
        self.db = self.client[db_name]
        self.pipeline = []

    def getCollection(self, coll_name:str):
        return self.db[coll_name]

    def queryCollection(self, coll_name:str, proj={}, filt={}):
        coll = self.getCollection(coll_name)
        results = coll.find(filt, proj)
        return list(results)
    
    def executePipeline(self, coll_name:str):
        coll = self.getCollection(coll_name)
        results = coll.aggregate(self.pipeline)
        return list(results)
    
    ## Aggregation functions go here

    def dropLevel(self, field):
        """
        Replaces the root document with the specified subdocument.

        Args:
            field (str): The field to use as the new root.

        Returns:
            list: A MongoDB aggregation stage.
        """
        stage = {
            '$replaceRoot': {'newRoot': f'${field}'}
        }
        return [stage]

    def nonNull(self, field):
        stage = {
            '$match':{
                field:{'$ne':None}
            }
        }

        return [stage]

    def match(self, conditions:list, match_all=False):
        """
        Creates a match stage for the aggregation pipeline.

        Args:
            conditions (list): A list of conditions to match.
            match_all (bool): Whether all conditions must be met (default is False).

        Returns:
            list: A MongoDB aggregation stage.
        """
        if match_all:
            stage = {
                '$match':{'$and':conditions}
            }
            return [stage]
        
        else:
            stage = {
                '$match':{'$or':conditions}
            }
        return [stage]

    def regex(self, field, rstr, match_case=False):
        """
        Creates a regex condition for the aggregation pipeline.

        Args:
            field (str): The field to apply the regex to.
            rstr (str): The regex string.
            match_case (bool): Whether the regex should be case-sensitive.

        Returns:
            dict: A MongoDB regex condition.
        """
        if match_case:
            option = ''
        elif match_case is False:
            option = 'i'

        stage = {
            f'{field}':{
                '$regex':f'{rstr}', '$options':f'{option}'
                }
            }
        return stage
    
    def project(self, fields:list):
        """
        Creates a projection stage for the aggregation pipeline.

        Args:
            fields (list): The fields to include in the projection.

        Returns:
            list: A MongoDB aggregation stage.
        """
        stage = {
            '$project':dict(zip(fields, [1]*len(fields)))
        }

        return [stage]
    
    def groupBy(self, fields, id_field, agg='first'):
        """
        Creates a group stage for the aggregation pipeline.

        Args:
            fields (list): Fields to include in the grouping.
            id_field (str): The field to group by.
            agg (str): The aggregation function to use (default is 'first').

        Returns:
            list: A MongoDB aggregation stage.
        """
        stage = {
            '$group': {
                '_id': f'${id_field}',
            }
        }

        for field in fields:
            stage['$group'][field] = {f'${agg}':f'${field}'}

        return [stage]

    def orderBy(self, orders:dict):
        """
        Creates a sort stage for the aggregation pipeline.

        Args:
            orders (dict): A dictionary of fields and sort orders.

        Returns:
            list: A MongoDB aggregation stage.
        """
        stage = {
            '$sort':orders
        }
        return [stage]

    def setField(self, old, new):
        """
        Renames a field in the aggregation pipeline.

        Args:
            old (str): The existing field name.
            new (str): The new field name.

        Returns:
            list: A MongoDB aggregation stage.
        """
        stage = {
            '$set':{new:f'${old}'}
        }
        return [stage]
    
    def unsetField(self, fields:list):
        """
        Removes specified fields in the aggregation pipeline.

        Args:
            fields (list): The fields to remove.

        Returns:
            list: A MongoDB aggregation stage.
        """
        stage = {
            '$unset':fields
        }
        return [stage]

    def limit(self, n:int):
        """
        Limits the number of documents in the aggregation pipeline.

        Args:
            n (int): The maximum number of documents.

        Returns:
            list: A MongoDB aggregation stage.
        """
        stage = {
            '$limit':n
        }

        return [stage]
    
    def ownRandom(self, n=50):
        sample = self.getCollection('items').update_many(
            {'$sample':{'size':n}},
            {'$setField':{
                'quantity_owned':2
            }}
        )

        print([i for i in sample])


if __name__ == '__main__':
    mongo = MongoManager('SmartCart')
    mongo.ownRandom()