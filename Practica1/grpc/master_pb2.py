# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: master.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cmaster.proto\x1a\x1bgoogle/protobuf/empty.proto\"\x18\n\x07\x41\x64\x64ress\x12\r\n\x05value\x18\x01 \x01(\t\"\x1a\n\tAddresses\x12\r\n\x05value\x18\x01 \x03(\t\"\x1d\n\x0c\x43onfirmation\x12\r\n\x05value\x18\x01 \x01(\x08\x32\x98\x01\n\x06Master\x12&\n\taddWorker\x12\x08.Address\x1a\r.Confirmation\"\x00\x12\x32\n\x0c\x64\x65leteWorker\x12\x08.Address\x1a\x16.google.protobuf.Empty\"\x00\x12\x32\n\ngetWorkers\x12\x16.google.protobuf.Empty\x1a\n.Addresses\"\x00\x62\x06proto3')



_ADDRESS = DESCRIPTOR.message_types_by_name['Address']
_ADDRESSES = DESCRIPTOR.message_types_by_name['Addresses']
_CONFIRMATION = DESCRIPTOR.message_types_by_name['Confirmation']
Address = _reflection.GeneratedProtocolMessageType('Address', (_message.Message,), {
  'DESCRIPTOR' : _ADDRESS,
  '__module__' : 'master_pb2'
  # @@protoc_insertion_point(class_scope:Address)
  })
_sym_db.RegisterMessage(Address)

Addresses = _reflection.GeneratedProtocolMessageType('Addresses', (_message.Message,), {
  'DESCRIPTOR' : _ADDRESSES,
  '__module__' : 'master_pb2'
  # @@protoc_insertion_point(class_scope:Addresses)
  })
_sym_db.RegisterMessage(Addresses)

Confirmation = _reflection.GeneratedProtocolMessageType('Confirmation', (_message.Message,), {
  'DESCRIPTOR' : _CONFIRMATION,
  '__module__' : 'master_pb2'
  # @@protoc_insertion_point(class_scope:Confirmation)
  })
_sym_db.RegisterMessage(Confirmation)

_MASTER = DESCRIPTOR.services_by_name['Master']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ADDRESS._serialized_start=45
  _ADDRESS._serialized_end=69
  _ADDRESSES._serialized_start=71
  _ADDRESSES._serialized_end=97
  _CONFIRMATION._serialized_start=99
  _CONFIRMATION._serialized_end=128
  _MASTER._serialized_start=131
  _MASTER._serialized_end=283
# @@protoc_insertion_point(module_scope)