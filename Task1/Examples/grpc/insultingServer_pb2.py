# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: insultingServer.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15insultingServer.proto\x1a\x1bgoogle/protobuf/empty.proto\"\x17\n\x06Insult\x12\r\n\x05value\x18\x01 \x01(\t\"\x18\n\x07Insults\x12\r\n\x05value\x18\x01 \x03(\t2\xa3\x01\n\x10InsultingService\x12\x30\n\ngetInsults\x12\x16.google.protobuf.Empty\x1a\x08.Insults\"\x00\x12.\n\taddInsult\x12\x07.Insult\x1a\x16.google.protobuf.Empty\"\x00\x12-\n\x08insultme\x12\x16.google.protobuf.Empty\x1a\x07.Insult\"\x00\x62\x06proto3')



_INSULT = DESCRIPTOR.message_types_by_name['Insult']
_INSULTS = DESCRIPTOR.message_types_by_name['Insults']
Insult = _reflection.GeneratedProtocolMessageType('Insult', (_message.Message,), {
  'DESCRIPTOR' : _INSULT,
  '__module__' : 'insultingServer_pb2'
  # @@protoc_insertion_point(class_scope:Insult)
  })
_sym_db.RegisterMessage(Insult)

Insults = _reflection.GeneratedProtocolMessageType('Insults', (_message.Message,), {
  'DESCRIPTOR' : _INSULTS,
  '__module__' : 'insultingServer_pb2'
  # @@protoc_insertion_point(class_scope:Insults)
  })
_sym_db.RegisterMessage(Insults)

_INSULTINGSERVICE = DESCRIPTOR.services_by_name['InsultingService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _INSULT._serialized_start=54
  _INSULT._serialized_end=77
  _INSULTS._serialized_start=79
  _INSULTS._serialized_end=103
  _INSULTINGSERVICE._serialized_start=106
  _INSULTINGSERVICE._serialized_end=269
# @@protoc_insertion_point(module_scope)
