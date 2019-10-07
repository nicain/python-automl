# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/automl_v1/proto/operations.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.cloud.automl_v1.proto import (
    io_pb2 as google_dot_cloud_dot_automl__v1_dot_proto_dot_io__pb2,
)
from google.cloud.automl_v1.proto import (
    model_pb2 as google_dot_cloud_dot_automl__v1_dot_proto_dot_model__pb2,
)
from google.cloud.automl_v1.proto import (
    model_evaluation_pb2 as google_dot_cloud_dot_automl__v1_dot_proto_dot_model__evaluation__pb2,
)
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/automl_v1/proto/operations.proto",
    package="google.cloud.automl.v1",
    syntax="proto3",
    serialized_options=_b(
        "\n\032com.google.cloud.automl.v1P\001Z<google.golang.org/genproto/googleapis/cloud/automl/v1;automl\252\002\026Google.Cloud.AutoML.V1\312\002\026Google\\Cloud\\AutoML\\V1\352\002\031Google::Cloud::AutoML::V1"
    ),
    serialized_pb=_b(
        '\n-google/cloud/automl_v1/proto/operations.proto\x12\x16google.cloud.automl.v1\x1a%google/cloud/automl_v1/proto/io.proto\x1a(google/cloud/automl_v1/proto/model.proto\x1a\x33google/cloud/automl_v1/proto/model_evaluation.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto\x1a\x1cgoogle/api/annotations.proto"\xe9\x02\n\x11OperationMetadata\x12I\n\x0e\x64\x65lete_details\x18\x08 \x01(\x0b\x32/.google.cloud.automl.v1.DeleteOperationMetadataH\x00\x12T\n\x14\x63reate_model_details\x18\n \x01(\x0b\x32\x34.google.cloud.automl.v1.CreateModelOperationMetadataH\x00\x12\x18\n\x10progress_percent\x18\r \x01(\x05\x12,\n\x10partial_failures\x18\x02 \x03(\x0b\x32\x12.google.rpc.Status\x12/\n\x0b\x63reate_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\t\n\x07\x64\x65tails"\x19\n\x17\x44\x65leteOperationMetadata"\x1e\n\x1c\x43reateModelOperationMetadataB\xaa\x01\n\x1a\x63om.google.cloud.automl.v1P\x01Z<google.golang.org/genproto/googleapis/cloud/automl/v1;automl\xaa\x02\x16Google.Cloud.AutoML.V1\xca\x02\x16Google\\Cloud\\AutoML\\V1\xea\x02\x19Google::Cloud::AutoML::V1b\x06proto3'
    ),
    dependencies=[
        google_dot_cloud_dot_automl__v1_dot_proto_dot_io__pb2.DESCRIPTOR,
        google_dot_cloud_dot_automl__v1_dot_proto_dot_model__pb2.DESCRIPTOR,
        google_dot_cloud_dot_automl__v1_dot_proto_dot_model__evaluation__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,
        google_dot_rpc_dot_status__pb2.DESCRIPTOR,
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
    ],
)


_OPERATIONMETADATA = _descriptor.Descriptor(
    name="OperationMetadata",
    full_name="google.cloud.automl.v1.OperationMetadata",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="delete_details",
            full_name="google.cloud.automl.v1.OperationMetadata.delete_details",
            index=0,
            number=8,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="create_model_details",
            full_name="google.cloud.automl.v1.OperationMetadata.create_model_details",
            index=1,
            number=10,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="progress_percent",
            full_name="google.cloud.automl.v1.OperationMetadata.progress_percent",
            index=2,
            number=13,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="partial_failures",
            full_name="google.cloud.automl.v1.OperationMetadata.partial_failures",
            index=3,
            number=2,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="create_time",
            full_name="google.cloud.automl.v1.OperationMetadata.create_time",
            index=4,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="update_time",
            full_name="google.cloud.automl.v1.OperationMetadata.update_time",
            index=5,
            number=4,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="details",
            full_name="google.cloud.automl.v1.OperationMetadata.details",
            index=0,
            containing_type=None,
            fields=[],
        )
    ],
    serialized_start=325,
    serialized_end=686,
)


_DELETEOPERATIONMETADATA = _descriptor.Descriptor(
    name="DeleteOperationMetadata",
    full_name="google.cloud.automl.v1.DeleteOperationMetadata",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=688,
    serialized_end=713,
)


_CREATEMODELOPERATIONMETADATA = _descriptor.Descriptor(
    name="CreateModelOperationMetadata",
    full_name="google.cloud.automl.v1.CreateModelOperationMetadata",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=715,
    serialized_end=745,
)

_OPERATIONMETADATA.fields_by_name[
    "delete_details"
].message_type = _DELETEOPERATIONMETADATA
_OPERATIONMETADATA.fields_by_name[
    "create_model_details"
].message_type = _CREATEMODELOPERATIONMETADATA
_OPERATIONMETADATA.fields_by_name[
    "partial_failures"
].message_type = google_dot_rpc_dot_status__pb2._STATUS
_OPERATIONMETADATA.fields_by_name[
    "create_time"
].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_OPERATIONMETADATA.fields_by_name[
    "update_time"
].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_OPERATIONMETADATA.oneofs_by_name["details"].fields.append(
    _OPERATIONMETADATA.fields_by_name["delete_details"]
)
_OPERATIONMETADATA.fields_by_name[
    "delete_details"
].containing_oneof = _OPERATIONMETADATA.oneofs_by_name["details"]
_OPERATIONMETADATA.oneofs_by_name["details"].fields.append(
    _OPERATIONMETADATA.fields_by_name["create_model_details"]
)
_OPERATIONMETADATA.fields_by_name[
    "create_model_details"
].containing_oneof = _OPERATIONMETADATA.oneofs_by_name["details"]
DESCRIPTOR.message_types_by_name["OperationMetadata"] = _OPERATIONMETADATA
DESCRIPTOR.message_types_by_name["DeleteOperationMetadata"] = _DELETEOPERATIONMETADATA
DESCRIPTOR.message_types_by_name[
    "CreateModelOperationMetadata"
] = _CREATEMODELOPERATIONMETADATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OperationMetadata = _reflection.GeneratedProtocolMessageType(
    "OperationMetadata",
    (_message.Message,),
    dict(
        DESCRIPTOR=_OPERATIONMETADATA,
        __module__="google.cloud.automl_v1.proto.operations_pb2",
        __doc__="""Metadata used across all long running operations returned by AutoML API.
  
  
  Attributes:
      details:
          Ouptut only. Details of specific operation. Even if this field
          is empty, the presence allows to distinguish different types
          of operations.
      delete_details:
          Details of a Delete operation.
      create_model_details:
          Details of CreateModel operation.
      progress_percent:
          Output only. Progress of operation. Range: [0, 100]. Not used
          currently.
      partial_failures:
          Output only. Partial failures encountered. E.g. single files
          that couldn't be read. This field should never exceed 20
          entries. Status details field will contain standard GCP error
          details.
      create_time:
          Output only. Time when the operation was created.
      update_time:
          Output only. Time when the operation was updated for the last
          time.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1.OperationMetadata)
    ),
)
_sym_db.RegisterMessage(OperationMetadata)

DeleteOperationMetadata = _reflection.GeneratedProtocolMessageType(
    "DeleteOperationMetadata",
    (_message.Message,),
    dict(
        DESCRIPTOR=_DELETEOPERATIONMETADATA,
        __module__="google.cloud.automl_v1.proto.operations_pb2",
        __doc__="""Details of operations that perform deletes of any entities.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1.DeleteOperationMetadata)
    ),
)
_sym_db.RegisterMessage(DeleteOperationMetadata)

CreateModelOperationMetadata = _reflection.GeneratedProtocolMessageType(
    "CreateModelOperationMetadata",
    (_message.Message,),
    dict(
        DESCRIPTOR=_CREATEMODELOPERATIONMETADATA,
        __module__="google.cloud.automl_v1.proto.operations_pb2",
        __doc__="""Details of CreateModel operation.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1.CreateModelOperationMetadata)
    ),
)
_sym_db.RegisterMessage(CreateModelOperationMetadata)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)