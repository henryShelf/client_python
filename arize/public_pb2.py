# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: public.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='public.proto',
  package='public',
  syntax='proto3',
  serialized_options=b'\n\022com.arize.protocolZ9github.com/Arize-ai/arize/go/pkg/receiver/protocol/public',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0cpublic.proto\x12\x06public\x1a\x1fgoogle/protobuf/timestamp.proto\"\x81\x01\n\nBulkRecord\x12\x18\n\x10organization_key\x18\x01 \x01(\t\x12\x10\n\x08model_id\x18\x02 \x01(\t\x12\x15\n\rmodel_version\x18\x03 \x01(\t\x12\x1f\n\x07records\x18\x05 \x03(\x0b\x32\x0e.public.RecordJ\x04\x08\x04\x10\x05R\ttimestamp\"\xa0\x02\n\x06Record\x12\x18\n\x10organization_key\x18\x01 \x01(\t\x12\x10\n\x08model_id\x18\x02 \x01(\t\x12\x15\n\rprediction_id\x18\x03 \x01(\t\x12&\n\nprediction\x18\x08 \x01(\x0b\x32\x12.public.Prediction\x12\x1e\n\x06\x61\x63tual\x18\t \x01(\x0b\x32\x0e.public.Actual\x12\x37\n\x13\x66\x65\x61ture_importances\x18\n \x01(\x0b\x32\x1a.public.FeatureImportances\x12:\n\x15prediction_and_actual\x18\x0b \x01(\x0b\x32\x1b.public.PredictionAndActualJ\x04\x08\x04\x10\x05J\x04\x08\x05\x10\x06J\x04\x08\x06\x10\x07J\x04\x08\x07\x10\x08\"\xae\x02\n\x13PreProductionRecord\x12\x45\n\x0ftraining_record\x18\x01 \x01(\x0b\x32*.public.PreProductionRecord.TrainingRecordH\x00\x12I\n\x11validation_record\x18\x02 \x01(\x0b\x32,.public.PreProductionRecord.ValidationRecordH\x00\x1a\x44\n\x10ValidationRecord\x12\x10\n\x08\x62\x61tch_id\x18\x01 \x01(\t\x12\x1e\n\x06record\x18\x02 \x01(\x0b\x32\x0e.public.Record\x1a\x30\n\x0eTrainingRecord\x12\x1e\n\x06record\x18\x01 \x01(\x0b\x32\x0e.public.RecordB\r\n\x0brecord_type\"6\n\x10ScoreCategorical\x12\x13\n\x0b\x63\x61tegorical\x18\x01 \x01(\t\x12\r\n\x05score\x18\x02 \x01(\x01\"\x82\x01\n\x05Label\x12\x10\n\x06\x62inary\x18\x01 \x01(\x08H\x00\x12\x15\n\x0b\x63\x61tegorical\x18\x02 \x01(\tH\x00\x12\x11\n\x07numeric\x18\x03 \x01(\x01H\x00\x12\x35\n\x11score_categorical\x18\x04 \x01(\x0b\x32\x18.public.ScoreCategoricalH\x00\x42\x06\n\x04\x64\x61ta\"\xe4\x01\n\nPrediction\x12-\n\ttimestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x15\n\rmodel_version\x18\x02 \x01(\t\x12\x1c\n\x05label\x18\x03 \x01(\x0b\x32\r.public.Label\x12\x32\n\x08\x66\x65\x61tures\x18\x04 \x03(\x0b\x32 .public.Prediction.FeaturesEntry\x1a>\n\rFeaturesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1c\n\x05value\x18\x02 \x01(\x0b\x32\r.public.Value:\x02\x38\x01\"m\n\x05Value\x12\x10\n\x06string\x18\x01 \x01(\tH\x00\x12\r\n\x03int\x18\x02 \x01(\x03H\x00\x12\x10\n\x06\x64ouble\x18\x03 \x01(\x01H\x00\x12)\n\x0bmulti_value\x18\x04 \x01(\x0b\x32\x12.public.MultiValueH\x00\x42\x06\n\x04\x64\x61ta\"\x1c\n\nMultiValue\x12\x0e\n\x06values\x18\x01 \x03(\t\"U\n\x06\x41\x63tual\x12-\n\ttimestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1c\n\x05label\x18\x02 \x01(\x0b\x32\r.public.Label\"\xe6\x01\n\x12\x46\x65\x61tureImportances\x12-\n\ttimestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x15\n\rmodel_version\x18\x02 \x01(\t\x12O\n\x13\x66\x65\x61ture_importances\x18\x03 \x03(\x0b\x32\x32.public.FeatureImportances.FeatureImportancesEntry\x1a\x39\n\x17\x46\x65\x61tureImportancesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x01:\x02\x38\x01\"]\n\x13PredictionAndActual\x12&\n\nprediction\x18\x01 \x01(\x0b\x32\x12.public.Prediction\x12\x1e\n\x06\x61\x63tual\x18\x02 \x01(\x0b\x32\x0e.public.Actual*8\n\x0b\x45nvironment\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0c\n\x08TRAINING\x10\x01\x12\x0e\n\nVALIDATION\x10\x02\x42O\n\x12\x63om.arize.protocolZ9github.com/Arize-ai/arize/go/pkg/receiver/protocol/publicb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])

_ENVIRONMENT = _descriptor.EnumDescriptor(
  name='Environment',
  full_name='public.Environment',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TRAINING', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='VALIDATION', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1761,
  serialized_end=1817,
)
_sym_db.RegisterEnumDescriptor(_ENVIRONMENT)

Environment = enum_type_wrapper.EnumTypeWrapper(_ENVIRONMENT)
UNKNOWN = 0
TRAINING = 1
VALIDATION = 2



_BULKRECORD = _descriptor.Descriptor(
  name='BulkRecord',
  full_name='public.BulkRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='organization_key', full_name='public.BulkRecord.organization_key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='model_id', full_name='public.BulkRecord.model_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='model_version', full_name='public.BulkRecord.model_version', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='records', full_name='public.BulkRecord.records', index=3,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_end=187,
)


_RECORD = _descriptor.Descriptor(
  name='Record',
  full_name='public.Record',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='organization_key', full_name='public.Record.organization_key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='model_id', full_name='public.Record.model_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='prediction_id', full_name='public.Record.prediction_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='prediction', full_name='public.Record.prediction', index=3,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='actual', full_name='public.Record.actual', index=4,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='feature_importances', full_name='public.Record.feature_importances', index=5,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='prediction_and_actual', full_name='public.Record.prediction_and_actual', index=6,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=190,
  serialized_end=478,
)


_PREPRODUCTIONRECORD_VALIDATIONRECORD = _descriptor.Descriptor(
  name='ValidationRecord',
  full_name='public.PreProductionRecord.ValidationRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='batch_id', full_name='public.PreProductionRecord.ValidationRecord.batch_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='record', full_name='public.PreProductionRecord.ValidationRecord.record', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=650,
  serialized_end=718,
)

_PREPRODUCTIONRECORD_TRAININGRECORD = _descriptor.Descriptor(
  name='TrainingRecord',
  full_name='public.PreProductionRecord.TrainingRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='record', full_name='public.PreProductionRecord.TrainingRecord.record', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=720,
  serialized_end=768,
)

_PREPRODUCTIONRECORD = _descriptor.Descriptor(
  name='PreProductionRecord',
  full_name='public.PreProductionRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='training_record', full_name='public.PreProductionRecord.training_record', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='validation_record', full_name='public.PreProductionRecord.validation_record', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_PREPRODUCTIONRECORD_VALIDATIONRECORD, _PREPRODUCTIONRECORD_TRAININGRECORD, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='record_type', full_name='public.PreProductionRecord.record_type',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=481,
  serialized_end=783,
)


_SCORECATEGORICAL = _descriptor.Descriptor(
  name='ScoreCategorical',
  full_name='public.ScoreCategorical',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='categorical', full_name='public.ScoreCategorical.categorical', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='score', full_name='public.ScoreCategorical.score', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=785,
  serialized_end=839,
)


_LABEL = _descriptor.Descriptor(
  name='Label',
  full_name='public.Label',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='binary', full_name='public.Label.binary', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='categorical', full_name='public.Label.categorical', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='numeric', full_name='public.Label.numeric', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='score_categorical', full_name='public.Label.score_categorical', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='data', full_name='public.Label.data',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=842,
  serialized_end=972,
)


_PREDICTION_FEATURESENTRY = _descriptor.Descriptor(
  name='FeaturesEntry',
  full_name='public.Prediction.FeaturesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='public.Prediction.FeaturesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='public.Prediction.FeaturesEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=1141,
  serialized_end=1203,
)

_PREDICTION = _descriptor.Descriptor(
  name='Prediction',
  full_name='public.Prediction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='public.Prediction.timestamp', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='model_version', full_name='public.Prediction.model_version', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='label', full_name='public.Prediction.label', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='features', full_name='public.Prediction.features', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_PREDICTION_FEATURESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=975,
  serialized_end=1203,
)


_VALUE = _descriptor.Descriptor(
  name='Value',
  full_name='public.Value',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='string', full_name='public.Value.string', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='int', full_name='public.Value.int', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='double', full_name='public.Value.double', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='multi_value', full_name='public.Value.multi_value', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='data', full_name='public.Value.data',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=1205,
  serialized_end=1314,
)


_MULTIVALUE = _descriptor.Descriptor(
  name='MultiValue',
  full_name='public.MultiValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='values', full_name='public.MultiValue.values', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1316,
  serialized_end=1344,
)


_ACTUAL = _descriptor.Descriptor(
  name='Actual',
  full_name='public.Actual',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='public.Actual.timestamp', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='label', full_name='public.Actual.label', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=1346,
  serialized_end=1431,
)


_FEATUREIMPORTANCES_FEATUREIMPORTANCESENTRY = _descriptor.Descriptor(
  name='FeatureImportancesEntry',
  full_name='public.FeatureImportances.FeatureImportancesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='public.FeatureImportances.FeatureImportancesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='public.FeatureImportances.FeatureImportancesEntry.value', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=1607,
  serialized_end=1664,
)

_FEATUREIMPORTANCES = _descriptor.Descriptor(
  name='FeatureImportances',
  full_name='public.FeatureImportances',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='public.FeatureImportances.timestamp', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='model_version', full_name='public.FeatureImportances.model_version', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='feature_importances', full_name='public.FeatureImportances.feature_importances', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_FEATUREIMPORTANCES_FEATUREIMPORTANCESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1434,
  serialized_end=1664,
)


_PREDICTIONANDACTUAL = _descriptor.Descriptor(
  name='PredictionAndActual',
  full_name='public.PredictionAndActual',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='prediction', full_name='public.PredictionAndActual.prediction', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='actual', full_name='public.PredictionAndActual.actual', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=1666,
  serialized_end=1759,
)

_BULKRECORD.fields_by_name['records'].message_type = _RECORD
_RECORD.fields_by_name['prediction'].message_type = _PREDICTION
_RECORD.fields_by_name['actual'].message_type = _ACTUAL
_RECORD.fields_by_name['feature_importances'].message_type = _FEATUREIMPORTANCES
_RECORD.fields_by_name['prediction_and_actual'].message_type = _PREDICTIONANDACTUAL
_PREPRODUCTIONRECORD_VALIDATIONRECORD.fields_by_name['record'].message_type = _RECORD
_PREPRODUCTIONRECORD_VALIDATIONRECORD.containing_type = _PREPRODUCTIONRECORD
_PREPRODUCTIONRECORD_TRAININGRECORD.fields_by_name['record'].message_type = _RECORD
_PREPRODUCTIONRECORD_TRAININGRECORD.containing_type = _PREPRODUCTIONRECORD
_PREPRODUCTIONRECORD.fields_by_name['training_record'].message_type = _PREPRODUCTIONRECORD_TRAININGRECORD
_PREPRODUCTIONRECORD.fields_by_name['validation_record'].message_type = _PREPRODUCTIONRECORD_VALIDATIONRECORD
_PREPRODUCTIONRECORD.oneofs_by_name['record_type'].fields.append(
  _PREPRODUCTIONRECORD.fields_by_name['training_record'])
_PREPRODUCTIONRECORD.fields_by_name['training_record'].containing_oneof = _PREPRODUCTIONRECORD.oneofs_by_name['record_type']
_PREPRODUCTIONRECORD.oneofs_by_name['record_type'].fields.append(
  _PREPRODUCTIONRECORD.fields_by_name['validation_record'])
_PREPRODUCTIONRECORD.fields_by_name['validation_record'].containing_oneof = _PREPRODUCTIONRECORD.oneofs_by_name['record_type']
_LABEL.fields_by_name['score_categorical'].message_type = _SCORECATEGORICAL
_LABEL.oneofs_by_name['data'].fields.append(
  _LABEL.fields_by_name['binary'])
_LABEL.fields_by_name['binary'].containing_oneof = _LABEL.oneofs_by_name['data']
_LABEL.oneofs_by_name['data'].fields.append(
  _LABEL.fields_by_name['categorical'])
_LABEL.fields_by_name['categorical'].containing_oneof = _LABEL.oneofs_by_name['data']
_LABEL.oneofs_by_name['data'].fields.append(
  _LABEL.fields_by_name['numeric'])
_LABEL.fields_by_name['numeric'].containing_oneof = _LABEL.oneofs_by_name['data']
_LABEL.oneofs_by_name['data'].fields.append(
  _LABEL.fields_by_name['score_categorical'])
_LABEL.fields_by_name['score_categorical'].containing_oneof = _LABEL.oneofs_by_name['data']
_PREDICTION_FEATURESENTRY.fields_by_name['value'].message_type = _VALUE
_PREDICTION_FEATURESENTRY.containing_type = _PREDICTION
_PREDICTION.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_PREDICTION.fields_by_name['label'].message_type = _LABEL
_PREDICTION.fields_by_name['features'].message_type = _PREDICTION_FEATURESENTRY
_VALUE.fields_by_name['multi_value'].message_type = _MULTIVALUE
_VALUE.oneofs_by_name['data'].fields.append(
  _VALUE.fields_by_name['string'])
_VALUE.fields_by_name['string'].containing_oneof = _VALUE.oneofs_by_name['data']
_VALUE.oneofs_by_name['data'].fields.append(
  _VALUE.fields_by_name['int'])
_VALUE.fields_by_name['int'].containing_oneof = _VALUE.oneofs_by_name['data']
_VALUE.oneofs_by_name['data'].fields.append(
  _VALUE.fields_by_name['double'])
_VALUE.fields_by_name['double'].containing_oneof = _VALUE.oneofs_by_name['data']
_VALUE.oneofs_by_name['data'].fields.append(
  _VALUE.fields_by_name['multi_value'])
_VALUE.fields_by_name['multi_value'].containing_oneof = _VALUE.oneofs_by_name['data']
_ACTUAL.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ACTUAL.fields_by_name['label'].message_type = _LABEL
_FEATUREIMPORTANCES_FEATUREIMPORTANCESENTRY.containing_type = _FEATUREIMPORTANCES
_FEATUREIMPORTANCES.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_FEATUREIMPORTANCES.fields_by_name['feature_importances'].message_type = _FEATUREIMPORTANCES_FEATUREIMPORTANCESENTRY
_PREDICTIONANDACTUAL.fields_by_name['prediction'].message_type = _PREDICTION
_PREDICTIONANDACTUAL.fields_by_name['actual'].message_type = _ACTUAL
DESCRIPTOR.message_types_by_name['BulkRecord'] = _BULKRECORD
DESCRIPTOR.message_types_by_name['Record'] = _RECORD
DESCRIPTOR.message_types_by_name['PreProductionRecord'] = _PREPRODUCTIONRECORD
DESCRIPTOR.message_types_by_name['ScoreCategorical'] = _SCORECATEGORICAL
DESCRIPTOR.message_types_by_name['Label'] = _LABEL
DESCRIPTOR.message_types_by_name['Prediction'] = _PREDICTION
DESCRIPTOR.message_types_by_name['Value'] = _VALUE
DESCRIPTOR.message_types_by_name['MultiValue'] = _MULTIVALUE
DESCRIPTOR.message_types_by_name['Actual'] = _ACTUAL
DESCRIPTOR.message_types_by_name['FeatureImportances'] = _FEATUREIMPORTANCES
DESCRIPTOR.message_types_by_name['PredictionAndActual'] = _PREDICTIONANDACTUAL
DESCRIPTOR.enum_types_by_name['Environment'] = _ENVIRONMENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BulkRecord = _reflection.GeneratedProtocolMessageType('BulkRecord', (_message.Message,), {
  'DESCRIPTOR' : _BULKRECORD,
  '__module__' : 'public_pb2'
  # @@protoc_insertion_point(class_scope:public.BulkRecord)
  })
_sym_db.RegisterMessage(BulkRecord)

Record = _reflection.GeneratedProtocolMessageType('Record', (_message.Message,), {
  'DESCRIPTOR' : _RECORD,
  '__module__' : 'public_pb2'
  # @@protoc_insertion_point(class_scope:public.Record)
  })
_sym_db.RegisterMessage(Record)

PreProductionRecord = _reflection.GeneratedProtocolMessageType('PreProductionRecord', (_message.Message,), {

  'ValidationRecord' : _reflection.GeneratedProtocolMessageType('ValidationRecord', (_message.Message,), {
    'DESCRIPTOR' : _PREPRODUCTIONRECORD_VALIDATIONRECORD,
    '__module__' : 'public_pb2'
    # @@protoc_insertion_point(class_scope:public.PreProductionRecord.ValidationRecord)
    })
  ,

  'TrainingRecord' : _reflection.GeneratedProtocolMessageType('TrainingRecord', (_message.Message,), {
    'DESCRIPTOR' : _PREPRODUCTIONRECORD_TRAININGRECORD,
    '__module__' : 'public_pb2'
    # @@protoc_insertion_point(class_scope:public.PreProductionRecord.TrainingRecord)
    })
  ,
  'DESCRIPTOR' : _PREPRODUCTIONRECORD,
  '__module__' : 'public_pb2'
  # @@protoc_insertion_point(class_scope:public.PreProductionRecord)
  })
_sym_db.RegisterMessage(PreProductionRecord)
_sym_db.RegisterMessage(PreProductionRecord.ValidationRecord)
_sym_db.RegisterMessage(PreProductionRecord.TrainingRecord)

ScoreCategorical = _reflection.GeneratedProtocolMessageType('ScoreCategorical', (_message.Message,), {
  'DESCRIPTOR' : _SCORECATEGORICAL,
  '__module__' : 'public_pb2'
  # @@protoc_insertion_point(class_scope:public.ScoreCategorical)
  })
_sym_db.RegisterMessage(ScoreCategorical)

Label = _reflection.GeneratedProtocolMessageType('Label', (_message.Message,), {
  'DESCRIPTOR' : _LABEL,
  '__module__' : 'public_pb2'
  # @@protoc_insertion_point(class_scope:public.Label)
  })
_sym_db.RegisterMessage(Label)

Prediction = _reflection.GeneratedProtocolMessageType('Prediction', (_message.Message,), {

  'FeaturesEntry' : _reflection.GeneratedProtocolMessageType('FeaturesEntry', (_message.Message,), {
    'DESCRIPTOR' : _PREDICTION_FEATURESENTRY,
    '__module__' : 'public_pb2'
    # @@protoc_insertion_point(class_scope:public.Prediction.FeaturesEntry)
    })
  ,
  'DESCRIPTOR' : _PREDICTION,
  '__module__' : 'public_pb2'
  # @@protoc_insertion_point(class_scope:public.Prediction)
  })
_sym_db.RegisterMessage(Prediction)
_sym_db.RegisterMessage(Prediction.FeaturesEntry)

Value = _reflection.GeneratedProtocolMessageType('Value', (_message.Message,), {
  'DESCRIPTOR' : _VALUE,
  '__module__' : 'public_pb2'
  # @@protoc_insertion_point(class_scope:public.Value)
  })
_sym_db.RegisterMessage(Value)

MultiValue = _reflection.GeneratedProtocolMessageType('MultiValue', (_message.Message,), {
  'DESCRIPTOR' : _MULTIVALUE,
  '__module__' : 'public_pb2'
  # @@protoc_insertion_point(class_scope:public.MultiValue)
  })
_sym_db.RegisterMessage(MultiValue)

Actual = _reflection.GeneratedProtocolMessageType('Actual', (_message.Message,), {
  'DESCRIPTOR' : _ACTUAL,
  '__module__' : 'public_pb2'
  # @@protoc_insertion_point(class_scope:public.Actual)
  })
_sym_db.RegisterMessage(Actual)

FeatureImportances = _reflection.GeneratedProtocolMessageType('FeatureImportances', (_message.Message,), {

  'FeatureImportancesEntry' : _reflection.GeneratedProtocolMessageType('FeatureImportancesEntry', (_message.Message,), {
    'DESCRIPTOR' : _FEATUREIMPORTANCES_FEATUREIMPORTANCESENTRY,
    '__module__' : 'public_pb2'
    # @@protoc_insertion_point(class_scope:public.FeatureImportances.FeatureImportancesEntry)
    })
  ,
  'DESCRIPTOR' : _FEATUREIMPORTANCES,
  '__module__' : 'public_pb2'
  # @@protoc_insertion_point(class_scope:public.FeatureImportances)
  })
_sym_db.RegisterMessage(FeatureImportances)
_sym_db.RegisterMessage(FeatureImportances.FeatureImportancesEntry)

PredictionAndActual = _reflection.GeneratedProtocolMessageType('PredictionAndActual', (_message.Message,), {
  'DESCRIPTOR' : _PREDICTIONANDACTUAL,
  '__module__' : 'public_pb2'
  # @@protoc_insertion_point(class_scope:public.PredictionAndActual)
  })
_sym_db.RegisterMessage(PredictionAndActual)


DESCRIPTOR._options = None
_PREDICTION_FEATURESENTRY._options = None
_FEATUREIMPORTANCES_FEATUREIMPORTANCESENTRY._options = None
# @@protoc_insertion_point(module_scope)
