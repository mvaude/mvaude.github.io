# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: resume.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cresume.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xe4\x02\n\x06Resume\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x13\n\x0bsource_code\x18\x03 \x01(\t\x12\x11\n\thost_link\x18\x04 \x01(\t\x12\'\n\x0cphone_number\x18\x05 \x01(\x0b\x32\x0c.PhoneNumberH\x00\x88\x01\x01\x12 \n\x08location\x18\x06 \x01(\x0b\x32\t.LocationH\x01\x88\x01\x01\x12\x18\n\x10linkedin_profile\x18\x07 \x01(\t\x12\x16\n\x0egithub_profile\x18\x08 \x01(\t\x12\x1a\n\x08\x61\x62out_me\x18\t \x03(\x0b\x32\x08.AboutMe\x12\x1d\n\teducation\x18\n \x03(\x0b\x32\n.Education\x12\x1f\n\nexperience\x18\x0b \x03(\x0b\x32\x0b.Experience\x12\x1e\n\x06skills\x18\x0c \x03(\x0b\x32\x0e.SkillCategoryB\x0f\n\r_phone_numberB\x0b\n\t_location\"\x1e\n\x07\x41\x62outMe\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\"3\n\x0bPhoneNumber\x12\x14\n\x0c\x63ountry_code\x18\x01 \x01(\r\x12\x0e\n\x06number\x18\x02 \x01(\x04\"G\n\x08Location\x12\x0c\n\x04\x63ity\x18\x01 \x01(\t\x12\x12\n\x05state\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x0f\n\x07\x63ountry\x18\x03 \x01(\tB\x08\n\x06_state\"_\n\tDateRange\x12)\n\x05start\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\'\n\x03\x65nd\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xe2\x01\n\tEducation\x12\x13\n\x0binstitution\x18\x01 \x01(\t\x12\r\n\x05major\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x1a\n\x06period\x18\x04 \x01(\x0b\x32\n.DateRange\x12!\n\x06\x64\x65gree\x18\x05 \x01(\x0e\x32\x11.Education.Degree\x12\x1b\n\x08location\x18\x06 \x01(\x0b\x32\t.Location\"@\n\x06\x44\x65gree\x12\x10\n\x0c\x42\x61\x63\x63\x61laureat\x10\x00\x12\r\n\tBACHELORS\x10\x01\x12\x0b\n\x07MASTERS\x10\x02\x12\x08\n\x04MOOC\x10\x03\"\x90\x01\n\nExperience\x12\r\n\x05title\x18\x01 \x01(\t\x12\x14\n\x0corganization\x18\x02 \x01(\t\x12\x0f\n\x07website\x18\x03 \x01(\t\x12\x1a\n\x06period\x18\x04 \x01(\x0b\x32\n.DateRange\x12\x1b\n\x08location\x18\x05 \x01(\x0b\x32\t.Location\x12\x13\n\x04\x64uty\x18\x06 \x03(\x0b\x32\x05.Duty\"7\n\x04\x44uty\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x0c\n\x04tags\x18\x02 \x03(\t\x12\x0c\n\x04\x64\x65mo\x18\x03 \x01(\t\"/\n\rSkillCategory\x12\x10\n\x08\x63\x61tegory\x18\x01 \x01(\t\x12\x0c\n\x04tags\x18\x02 \x03(\tb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'resume_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _RESUME._serialized_start=50
  _RESUME._serialized_end=406
  _ABOUTME._serialized_start=408
  _ABOUTME._serialized_end=438
  _PHONENUMBER._serialized_start=440
  _PHONENUMBER._serialized_end=491
  _LOCATION._serialized_start=493
  _LOCATION._serialized_end=564
  _DATERANGE._serialized_start=566
  _DATERANGE._serialized_end=661
  _EDUCATION._serialized_start=664
  _EDUCATION._serialized_end=890
  _EDUCATION_DEGREE._serialized_start=826
  _EDUCATION_DEGREE._serialized_end=890
  _EXPERIENCE._serialized_start=893
  _EXPERIENCE._serialized_end=1037
  _DUTY._serialized_start=1039
  _DUTY._serialized_end=1094
  _SKILLCATEGORY._serialized_start=1096
  _SKILLCATEGORY._serialized_end=1143
# @@protoc_insertion_point(module_scope)