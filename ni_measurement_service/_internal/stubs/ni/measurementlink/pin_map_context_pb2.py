# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ni/measurementlink/pin_map_context.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="ni/measurementlink/pin_map_context.proto",
    package="ni.measurementlink",
    syntax="proto3",
    serialized_options=b"\n\026com.ni.measurementlinkB\022PinMapContextProtoP\001Z\017pinmapcontextv1\242\002\003NIM\252\002#NationalInstruments.MeasurementLink\312\002\022NI\\MeasurementLink\352\002\023NI::MeasurementLink",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n(ni/measurementlink/pin_map_context.proto\x12\x12ni.measurementlink"2\n\rPinMapContext\x12\x12\n\npin_map_id\x18\x01 \x01(\t\x12\r\n\x05sites\x18\x02 \x03(\x05\x42\x96\x01\n\x16\x63om.ni.measurementlinkB\x12PinMapContextProtoP\x01Z\x0fpinmapcontextv1\xa2\x02\x03NIM\xaa\x02#NationalInstruments.MeasurementLink\xca\x02\x12NI\\MeasurementLink\xea\x02\x13NI::MeasurementLinkb\x06proto3',
)


_PINMAPCONTEXT = _descriptor.Descriptor(
    name="PinMapContext",
    full_name="ni.measurementlink.PinMapContext",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="pin_map_id",
            full_name="ni.measurementlink.PinMapContext.pin_map_id",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="sites",
            full_name="ni.measurementlink.PinMapContext.sites",
            index=1,
            number=2,
            type=5,
            cpp_type=1,
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
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=64,
    serialized_end=114,
)

DESCRIPTOR.message_types_by_name["PinMapContext"] = _PINMAPCONTEXT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PinMapContext = _reflection.GeneratedProtocolMessageType(
    "PinMapContext",
    (_message.Message,),
    {
        "DESCRIPTOR": _PINMAPCONTEXT,
        "__module__": "ni.measurementlink.pin_map_context_pb2"
        # @@protoc_insertion_point(class_scope:ni.measurementlink.PinMapContext)
    },
)
_sym_db.RegisterMessage(PinMapContext)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)