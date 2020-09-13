# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: keyvalue.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='keyvalue.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0ekeyvalue.proto\"&\n\x08KeyValue\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"\x12\n\x03Key\x12\x0b\n\x03key\x18\x01 \x01(\x05\"\'\n\x05Value\x12\r\n\x05value\x18\x01 \x01(\t\x12\x0f\n\x07\x64\x65\x66ined\x18\x02 \x01(\x08\")\n\x0bNewKeyValue\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"\x06\n\x04Void\"a\n\nStoredKeys\x12%\n\x05store\x18\x01 \x03(\x0b\x32\x16.StoredKeys.StoreEntry\x1a,\n\nStoreEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x32j\n\x0fKeyValueService\x12\x15\n\x03get\x12\x04.Key\x1a\x06.Value\"\x00\x12\x1c\n\x03put\x12\x0c.NewKeyValue\x1a\x05.Void\"\x00\x12\"\n\ngetAllKeys\x12\x05.Void\x1a\x0b.StoredKeys\"\x00\x62\x06proto3'
)




_KEYVALUE = _descriptor.Descriptor(
  name='KeyValue',
  full_name='KeyValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='KeyValue.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='KeyValue.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=56,
)


_KEY = _descriptor.Descriptor(
  name='Key',
  full_name='Key',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='Key.key', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=58,
  serialized_end=76,
)


_VALUE = _descriptor.Descriptor(
  name='Value',
  full_name='Value',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='Value.value', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='defined', full_name='Value.defined', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=78,
  serialized_end=117,
)


_NEWKEYVALUE = _descriptor.Descriptor(
  name='NewKeyValue',
  full_name='NewKeyValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='NewKeyValue.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='NewKeyValue.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=119,
  serialized_end=160,
)


_VOID = _descriptor.Descriptor(
  name='Void',
  full_name='Void',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=162,
  serialized_end=168,
)


_STOREDKEYS_STOREENTRY = _descriptor.Descriptor(
  name='StoreEntry',
  full_name='StoredKeys.StoreEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='StoredKeys.StoreEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='StoredKeys.StoreEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=223,
  serialized_end=267,
)

_STOREDKEYS = _descriptor.Descriptor(
  name='StoredKeys',
  full_name='StoredKeys',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='store', full_name='StoredKeys.store', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_STOREDKEYS_STOREENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=170,
  serialized_end=267,
)

_STOREDKEYS_STOREENTRY.containing_type = _STOREDKEYS
_STOREDKEYS.fields_by_name['store'].message_type = _STOREDKEYS_STOREENTRY
DESCRIPTOR.message_types_by_name['KeyValue'] = _KEYVALUE
DESCRIPTOR.message_types_by_name['Key'] = _KEY
DESCRIPTOR.message_types_by_name['Value'] = _VALUE
DESCRIPTOR.message_types_by_name['NewKeyValue'] = _NEWKEYVALUE
DESCRIPTOR.message_types_by_name['Void'] = _VOID
DESCRIPTOR.message_types_by_name['StoredKeys'] = _STOREDKEYS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

KeyValue = _reflection.GeneratedProtocolMessageType('KeyValue', (_message.Message,), {
  'DESCRIPTOR' : _KEYVALUE,
  '__module__' : 'keyvalue_pb2'
  # @@protoc_insertion_point(class_scope:KeyValue)
  })
_sym_db.RegisterMessage(KeyValue)

Key = _reflection.GeneratedProtocolMessageType('Key', (_message.Message,), {
  'DESCRIPTOR' : _KEY,
  '__module__' : 'keyvalue_pb2'
  # @@protoc_insertion_point(class_scope:Key)
  })
_sym_db.RegisterMessage(Key)

Value = _reflection.GeneratedProtocolMessageType('Value', (_message.Message,), {
  'DESCRIPTOR' : _VALUE,
  '__module__' : 'keyvalue_pb2'
  # @@protoc_insertion_point(class_scope:Value)
  })
_sym_db.RegisterMessage(Value)

NewKeyValue = _reflection.GeneratedProtocolMessageType('NewKeyValue', (_message.Message,), {
  'DESCRIPTOR' : _NEWKEYVALUE,
  '__module__' : 'keyvalue_pb2'
  # @@protoc_insertion_point(class_scope:NewKeyValue)
  })
_sym_db.RegisterMessage(NewKeyValue)

Void = _reflection.GeneratedProtocolMessageType('Void', (_message.Message,), {
  'DESCRIPTOR' : _VOID,
  '__module__' : 'keyvalue_pb2'
  # @@protoc_insertion_point(class_scope:Void)
  })
_sym_db.RegisterMessage(Void)

StoredKeys = _reflection.GeneratedProtocolMessageType('StoredKeys', (_message.Message,), {

  'StoreEntry' : _reflection.GeneratedProtocolMessageType('StoreEntry', (_message.Message,), {
    'DESCRIPTOR' : _STOREDKEYS_STOREENTRY,
    '__module__' : 'keyvalue_pb2'
    # @@protoc_insertion_point(class_scope:StoredKeys.StoreEntry)
    })
  ,
  'DESCRIPTOR' : _STOREDKEYS,
  '__module__' : 'keyvalue_pb2'
  # @@protoc_insertion_point(class_scope:StoredKeys)
  })
_sym_db.RegisterMessage(StoredKeys)
_sym_db.RegisterMessage(StoredKeys.StoreEntry)


_STOREDKEYS_STOREENTRY._options = None

_KEYVALUESERVICE = _descriptor.ServiceDescriptor(
  name='KeyValueService',
  full_name='KeyValueService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=269,
  serialized_end=375,
  methods=[
  _descriptor.MethodDescriptor(
    name='get',
    full_name='KeyValueService.get',
    index=0,
    containing_service=None,
    input_type=_KEY,
    output_type=_VALUE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='put',
    full_name='KeyValueService.put',
    index=1,
    containing_service=None,
    input_type=_NEWKEYVALUE,
    output_type=_VOID,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='getAllKeys',
    full_name='KeyValueService.getAllKeys',
    index=2,
    containing_service=None,
    input_type=_VOID,
    output_type=_STOREDKEYS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_KEYVALUESERVICE)

DESCRIPTOR.services_by_name['KeyValueService'] = _KEYVALUESERVICE

# @@protoc_insertion_point(module_scope)
