# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
from aliyunsdkaligreen_console.endpoint import endpoint_data

class AddSfacePersonRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'aligreen-console', '2019-11-15', 'AddSfacePerson')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_PersonGender(self):
		return self.get_query_params().get('PersonGender')

	def set_PersonGender(self,PersonGender):
		self.add_query_param('PersonGender',PersonGender)

	def get_PersonType(self):
		return self.get_query_params().get('PersonType')

	def set_PersonType(self,PersonType):
		self.add_query_param('PersonType',PersonType)

	def get_DataId(self):
		return self.get_query_params().get('DataId')

	def set_DataId(self,DataId):
		self.add_query_param('DataId',DataId)

	def get_FaceUrl(self):
		return self.get_query_params().get('FaceUrl')

	def set_FaceUrl(self,FaceUrl):
		self.add_query_param('FaceUrl',FaceUrl)

	def get_CallbackSeed(self):
		return self.get_query_params().get('CallbackSeed')

	def set_CallbackSeed(self,CallbackSeed):
		self.add_query_param('CallbackSeed',CallbackSeed)

	def get_CallbackUrl(self):
		return self.get_query_params().get('CallbackUrl')

	def set_CallbackUrl(self,CallbackUrl):
		self.add_query_param('CallbackUrl',CallbackUrl)

	def get_PersonName(self):
		return self.get_query_params().get('PersonName')

	def set_PersonName(self,PersonName):
		self.add_query_param('PersonName',PersonName)