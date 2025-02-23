# Copyright 2021 Zilliz. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import types


class BaseRepr:
    """Base representation from which all other representation objects inherit.
    Primarily implements automatic serialization into YAML/YAML-like string formats,
    along with defining other universally used properties.

    Args:
        name:
            Name of the internal object described by this representation.
    """

    def __init__(self, name: str):
        self._name = name

    @property
    def name(self):
        return self._name

    def serialize(self) -> str:
        """Universal function used to serialize this representation.

        Returns:
            A string containing the serialized version of this representation. Example
            output:

            'VariableRepr:
                name: variable
                vtype: tensor
                dtype: float'
        """
        out = self.__class__.__name___ + '\n'
        for name in dir(self):
            value = self.__getattribute__(name)
            if name[0] != '_' and not isinstance(value, types.FunctionType):
                value = value.__class__.__name__
                out += name + ': ' + str(value) + '\n'
        return out
