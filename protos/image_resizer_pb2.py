# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: object_detection/protos/image_resizer.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='object_detection/protos/image_resizer.proto',
  package='protos',
  syntax='proto2',
  serialized_pb=_b('\n+object_detection/protos/image_resizer.proto\x12\x06protos\"\xa4\x01\n\x0cImageResizer\x12\x43\n\x19keep_aspect_ratio_resizer\x18\x01 \x01(\x0b\x32\x1e.protos.KeepAspectRatioResizerH\x00\x12\x38\n\x13\x66ixed_shape_resizer\x18\x02 \x01(\x0b\x32\x19.protos.FixedShapeResizerH\x00\x42\x15\n\x13image_resizer_oneof\"\xd0\x01\n\x16KeepAspectRatioResizer\x12\x1a\n\rmin_dimension\x18\x01 \x01(\x05:\x03\x36\x30\x30\x12\x1b\n\rmax_dimension\x18\x02 \x01(\x05:\x04\x31\x30\x32\x34\x12\x33\n\rresize_method\x18\x03 \x01(\x0e\x32\x12.protos.ResizeType:\x08\x42ILINEAR\x12#\n\x14pad_to_max_dimension\x18\x04 \x01(\x08:\x05\x66\x61lse\x12#\n\x14\x63onvert_to_grayscale\x18\x05 \x01(\x08:\x05\x66\x61lse\"\x96\x01\n\x11\x46ixedShapeResizer\x12\x13\n\x06height\x18\x01 \x01(\x05:\x03\x33\x30\x30\x12\x12\n\x05width\x18\x02 \x01(\x05:\x03\x33\x30\x30\x12\x33\n\rresize_method\x18\x03 \x01(\x0e\x32\x12.protos.ResizeType:\x08\x42ILINEAR\x12#\n\x14\x63onvert_to_grayscale\x18\x04 \x01(\x08:\x05\x66\x61lse*G\n\nResizeType\x12\x0c\n\x08\x42ILINEAR\x10\x00\x12\x14\n\x10NEAREST_NEIGHBOR\x10\x01\x12\x0b\n\x07\x42ICUBIC\x10\x02\x12\x08\n\x04\x41REA\x10\x03')
)

_RESIZETYPE = _descriptor.EnumDescriptor(
  name='ResizeType',
  full_name='protos.ResizeType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BILINEAR', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NEAREST_NEIGHBOR', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BICUBIC', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AREA', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=586,
  serialized_end=657,
)
_sym_db.RegisterEnumDescriptor(_RESIZETYPE)

ResizeType = enum_type_wrapper.EnumTypeWrapper(_RESIZETYPE)
BILINEAR = 0
NEAREST_NEIGHBOR = 1
BICUBIC = 2
AREA = 3



_IMAGERESIZER = _descriptor.Descriptor(
  name='ImageResizer',
  full_name='protos.ImageResizer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='keep_aspect_ratio_resizer', full_name='protos.ImageResizer.keep_aspect_ratio_resizer', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fixed_shape_resizer', full_name='protos.ImageResizer.fixed_shape_resizer', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='image_resizer_oneof', full_name='protos.ImageResizer.image_resizer_oneof',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=56,
  serialized_end=220,
)


_KEEPASPECTRATIORESIZER = _descriptor.Descriptor(
  name='KeepAspectRatioResizer',
  full_name='protos.KeepAspectRatioResizer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='min_dimension', full_name='protos.KeepAspectRatioResizer.min_dimension', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=600,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_dimension', full_name='protos.KeepAspectRatioResizer.max_dimension', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=1024,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resize_method', full_name='protos.KeepAspectRatioResizer.resize_method', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pad_to_max_dimension', full_name='protos.KeepAspectRatioResizer.pad_to_max_dimension', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='convert_to_grayscale', full_name='protos.KeepAspectRatioResizer.convert_to_grayscale', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=223,
  serialized_end=431,
)


_FIXEDSHAPERESIZER = _descriptor.Descriptor(
  name='FixedShapeResizer',
  full_name='protos.FixedShapeResizer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='height', full_name='protos.FixedShapeResizer.height', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=300,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='width', full_name='protos.FixedShapeResizer.width', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=300,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resize_method', full_name='protos.FixedShapeResizer.resize_method', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='convert_to_grayscale', full_name='protos.FixedShapeResizer.convert_to_grayscale', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=434,
  serialized_end=584,
)

_IMAGERESIZER.fields_by_name['keep_aspect_ratio_resizer'].message_type = _KEEPASPECTRATIORESIZER
_IMAGERESIZER.fields_by_name['fixed_shape_resizer'].message_type = _FIXEDSHAPERESIZER
_IMAGERESIZER.oneofs_by_name['image_resizer_oneof'].fields.append(
  _IMAGERESIZER.fields_by_name['keep_aspect_ratio_resizer'])
_IMAGERESIZER.fields_by_name['keep_aspect_ratio_resizer'].containing_oneof = _IMAGERESIZER.oneofs_by_name['image_resizer_oneof']
_IMAGERESIZER.oneofs_by_name['image_resizer_oneof'].fields.append(
  _IMAGERESIZER.fields_by_name['fixed_shape_resizer'])
_IMAGERESIZER.fields_by_name['fixed_shape_resizer'].containing_oneof = _IMAGERESIZER.oneofs_by_name['image_resizer_oneof']
_KEEPASPECTRATIORESIZER.fields_by_name['resize_method'].enum_type = _RESIZETYPE
_FIXEDSHAPERESIZER.fields_by_name['resize_method'].enum_type = _RESIZETYPE
DESCRIPTOR.message_types_by_name['ImageResizer'] = _IMAGERESIZER
DESCRIPTOR.message_types_by_name['KeepAspectRatioResizer'] = _KEEPASPECTRATIORESIZER
DESCRIPTOR.message_types_by_name['FixedShapeResizer'] = _FIXEDSHAPERESIZER
DESCRIPTOR.enum_types_by_name['ResizeType'] = _RESIZETYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ImageResizer = _reflection.GeneratedProtocolMessageType('ImageResizer', (_message.Message,), dict(
  DESCRIPTOR = _IMAGERESIZER,
  __module__ = 'object_detection.protos.image_resizer_pb2'
  # @@protoc_insertion_point(class_scope:protos.ImageResizer)
  ))
_sym_db.RegisterMessage(ImageResizer)

KeepAspectRatioResizer = _reflection.GeneratedProtocolMessageType('KeepAspectRatioResizer', (_message.Message,), dict(
  DESCRIPTOR = _KEEPASPECTRATIORESIZER,
  __module__ = 'object_detection.protos.image_resizer_pb2'
  # @@protoc_insertion_point(class_scope:protos.KeepAspectRatioResizer)
  ))
_sym_db.RegisterMessage(KeepAspectRatioResizer)

FixedShapeResizer = _reflection.GeneratedProtocolMessageType('FixedShapeResizer', (_message.Message,), dict(
  DESCRIPTOR = _FIXEDSHAPERESIZER,
  __module__ = 'object_detection.protos.image_resizer_pb2'
  # @@protoc_insertion_point(class_scope:protos.FixedShapeResizer)
  ))
_sym_db.RegisterMessage(FixedShapeResizer)


# @@protoc_insertion_point(module_scope)
