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

from aliyunsdkbssopenapi.endpoint import endpoint_data
from aliyunsdkcore.request import RpcRequest


class SubscribeBillToOSSRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'BssOpenApi', '2017-12-14', 'SubscribeBillToOSS')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_SubscribeType(self):
		return self.get_query_params().get('SubscribeType')

	def set_SubscribeType(self,SubscribeType):
		self.add_query_param('SubscribeType',SubscribeType)

	def get_SubscribeBucket(self):
		return self.get_query_params().get('SubscribeBucket')

	def set_SubscribeBucket(self,SubscribeBucket):
		self.add_query_param('SubscribeBucket',SubscribeBucket)