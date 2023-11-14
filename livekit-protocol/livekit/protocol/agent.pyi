"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Copyright 2023 LiveKit, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
from . import models
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _JobType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _JobTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_JobType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    JT_ROOM: _JobType.ValueType  # 0
    JT_PUBLISHER: _JobType.ValueType  # 1

class JobType(_JobType, metaclass=_JobTypeEnumTypeWrapper): ...

JT_ROOM: JobType.ValueType  # 0
JT_PUBLISHER: JobType.ValueType  # 1
global___JobType = JobType

class _WorkerStatus:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _WorkerStatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_WorkerStatus.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    WS_AVAILABLE: _WorkerStatus.ValueType  # 0
    WS_FULL: _WorkerStatus.ValueType  # 1

class WorkerStatus(_WorkerStatus, metaclass=_WorkerStatusEnumTypeWrapper): ...

WS_AVAILABLE: WorkerStatus.ValueType  # 0
WS_FULL: WorkerStatus.ValueType  # 1
global___WorkerStatus = WorkerStatus

class _JobStatus:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _JobStatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_JobStatus.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    JS_UNKNOWN: _JobStatus.ValueType  # 0
    JS_SUCCESS: _JobStatus.ValueType  # 1
    JS_FAILED: _JobStatus.ValueType  # 2

class JobStatus(_JobStatus, metaclass=_JobStatusEnumTypeWrapper): ...

JS_UNKNOWN: JobStatus.ValueType  # 0
JS_SUCCESS: JobStatus.ValueType  # 1
JS_FAILED: JobStatus.ValueType  # 2
global___JobStatus = JobStatus

@typing_extensions.final
class AgentInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    id: builtins.str
    name: builtins.str
    version: builtins.str
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        name: builtins.str = ...,
        version: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["id", b"id", "name", b"name", "version", b"version"]) -> None: ...

global___AgentInfo = AgentInfo

@typing_extensions.final
class Job(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    ROOM_FIELD_NUMBER: builtins.int
    PARTICIPANT_FIELD_NUMBER: builtins.int
    id: builtins.str
    type: global___JobType.ValueType
    @property
    def room(self) -> models.Room: ...
    @property
    def participant(self) -> models.ParticipantInfo: ...
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        type: global___JobType.ValueType = ...,
        room: models.Room | None = ...,
        participant: models.ParticipantInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_participant", b"_participant", "participant", b"participant", "room", b"room"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_participant", b"_participant", "id", b"id", "participant", b"participant", "room", b"room", "type", b"type"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_participant", b"_participant"]) -> typing_extensions.Literal["participant"] | None: ...

global___Job = Job

@typing_extensions.final
class WorkerMessage(google.protobuf.message.Message):
    """from Worker to Server"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REGISTER_FIELD_NUMBER: builtins.int
    AVAILABILITY_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    JOB_UPDATE_FIELD_NUMBER: builtins.int
    @property
    def register(self) -> global___RegisterWorkerRequest:
        """agent workers need to register themselves with the server first"""
    @property
    def availability(self) -> global___AvailabilityResponse:
        """worker confirms to server that it's available for a job, or declines it"""
    @property
    def status(self) -> global___UpdateWorkerStatus:
        """worker can update its status to the server, including taking itself out of the pool"""
    @property
    def job_update(self) -> global___JobStatusUpdate: ...
    def __init__(
        self,
        *,
        register: global___RegisterWorkerRequest | None = ...,
        availability: global___AvailabilityResponse | None = ...,
        status: global___UpdateWorkerStatus | None = ...,
        job_update: global___JobStatusUpdate | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["availability", b"availability", "job_update", b"job_update", "message", b"message", "register", b"register", "status", b"status"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["availability", b"availability", "job_update", b"job_update", "message", b"message", "register", b"register", "status", b"status"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["message", b"message"]) -> typing_extensions.Literal["register", "availability", "status", "job_update"] | None: ...

global___WorkerMessage = WorkerMessage

@typing_extensions.final
class ServerMessage(google.protobuf.message.Message):
    """from Server to Worker"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REGISTER_FIELD_NUMBER: builtins.int
    AVAILABILITY_FIELD_NUMBER: builtins.int
    ASSIGNMENT_FIELD_NUMBER: builtins.int
    @property
    def register(self) -> global___RegisterWorkerResponse:
        """server confirms the registration, from this moment on, the worker is considered active"""
    @property
    def availability(self) -> global___AvailabilityRequest:
        """server asks worker to confirm availability for a job"""
    @property
    def assignment(self) -> global___JobAssignment: ...
    def __init__(
        self,
        *,
        register: global___RegisterWorkerResponse | None = ...,
        availability: global___AvailabilityRequest | None = ...,
        assignment: global___JobAssignment | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["assignment", b"assignment", "availability", b"availability", "message", b"message", "register", b"register"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["assignment", b"assignment", "availability", b"availability", "message", b"message", "register", b"register"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["message", b"message"]) -> typing_extensions.Literal["register", "availability", "assignment"] | None: ...

global___ServerMessage = ServerMessage

@typing_extensions.final
class RegisterWorkerRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TYPE_FIELD_NUMBER: builtins.int
    WORKER_ID_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    type: global___JobType.ValueType
    worker_id: builtins.str
    version: builtins.str
    name: builtins.str
    def __init__(
        self,
        *,
        type: global___JobType.ValueType = ...,
        worker_id: builtins.str = ...,
        version: builtins.str = ...,
        name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name", b"name", "type", b"type", "version", b"version", "worker_id", b"worker_id"]) -> None: ...

global___RegisterWorkerRequest = RegisterWorkerRequest

@typing_extensions.final
class RegisterWorkerResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    WORKER_ID_FIELD_NUMBER: builtins.int
    SERVER_VERSION_FIELD_NUMBER: builtins.int
    worker_id: builtins.str
    server_version: builtins.str
    def __init__(
        self,
        *,
        worker_id: builtins.str = ...,
        server_version: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["server_version", b"server_version", "worker_id", b"worker_id"]) -> None: ...

global___RegisterWorkerResponse = RegisterWorkerResponse

@typing_extensions.final
class AvailabilityRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    JOB_FIELD_NUMBER: builtins.int
    @property
    def job(self) -> global___Job: ...
    def __init__(
        self,
        *,
        job: global___Job | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["job", b"job"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["job", b"job"]) -> None: ...

global___AvailabilityRequest = AvailabilityRequest

@typing_extensions.final
class AvailabilityResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    JOB_ID_FIELD_NUMBER: builtins.int
    AVAILABLE_FIELD_NUMBER: builtins.int
    job_id: builtins.str
    available: builtins.bool
    def __init__(
        self,
        *,
        job_id: builtins.str = ...,
        available: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["available", b"available", "job_id", b"job_id"]) -> None: ...

global___AvailabilityResponse = AvailabilityResponse

@typing_extensions.final
class JobStatusUpdate(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    JOB_ID_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    ERROR_FIELD_NUMBER: builtins.int
    USER_DATA_FIELD_NUMBER: builtins.int
    job_id: builtins.str
    status: global___JobStatus.ValueType
    error: builtins.str
    user_data: builtins.str
    def __init__(
        self,
        *,
        job_id: builtins.str = ...,
        status: global___JobStatus.ValueType = ...,
        error: builtins.str = ...,
        user_data: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["error", b"error", "job_id", b"job_id", "status", b"status", "user_data", b"user_data"]) -> None: ...

global___JobStatusUpdate = JobStatusUpdate

@typing_extensions.final
class JobAssignment(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    JOB_FIELD_NUMBER: builtins.int
    @property
    def job(self) -> global___Job: ...
    def __init__(
        self,
        *,
        job: global___Job | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["job", b"job"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["job", b"job"]) -> None: ...

global___JobAssignment = JobAssignment

@typing_extensions.final
class UpdateWorkerStatus(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STATUS_FIELD_NUMBER: builtins.int
    status: global___WorkerStatus.ValueType
    def __init__(
        self,
        *,
        status: global___WorkerStatus.ValueType = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["status", b"status"]) -> None: ...

global___UpdateWorkerStatus = UpdateWorkerStatus