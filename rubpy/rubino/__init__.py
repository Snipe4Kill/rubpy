from rubpy import connections
from json import loads , dumps
from rubpy.encryption import Encryption
from random import choice
from rubpy.createMethod import createMethod

class Rubino(object):
	def __init__(self , auth : str) -> int:
		self.auth : str = auth
		self.Method = createMethod(auth)
		self.post : str = connections.post
		self.url : str = 'https://rubino12.iranlms.ir/'# ,# 'https://rubino1.iranlms.ir/'

	async def getPostByShareLink(self , post_link : str , profile_id : str) -> dict:
		"""
			Attention
			In the profile_id argument, you must enter the profile ID of your user account !
			post_link = https://rubika.ir/post/PBRLIJhLga
		"""
		data : dict = {
			"share_string" : post_link.split('/')[-1] if '/' in post_link else post_link,
			"profile_id" : profile_id
		}
		data : str = await self.Method.createMethod( 0 , "getPostByShareLink" , data)
		return loads(await self.post(self.url , data))

	async def getExplorePostTopics(self , profile_id : str) -> dict:
		"""
			Attention
			In the profile_id argument, you must enter the profile ID of your user account !
		"""
		data : dict = {
			"profile_id" : profile_id
		}
		data : str = await self.Method.createMethod( 0 , "getExplorePostTopics" , data)
		return loads(await self.post(self.url , data))

	async def getExplorePosts(self , profile_id : str , max_id: str) -> dict:
		"""
			Attention
			In the profile_id argument, you must enter the profile ID of your user account !
		"""
		data : dict = {
			"profile_id" : profile_id,
			"equal" : False,
			"limit" : 50,
			"max_id" : max_id,
			"sort" : "FromMax",
		}
		data : str = await self.Method.createMethod( 0 , "getExplorePosts" , data)
		return loads(await self.post(self.url , data))
