"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
---------------------------------------------------------------------
---------------------------------------------------------------------
"""

import abc
import collections.abc
import grpc
import grpc.aio
import ni_measurement_plugin_sdk_service._internal.stubs.ni.measurementlink.measurement.v1.measurement_service_pb2 as ni_measurementlink_measurement_v1_measurement_service_pb2
import typing

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class MeasurementServiceStub:
    """Service that implements a measurement. Unlike other services, a MeasurementService is designed to be a plugin
    where there can be multiple implementations of the service that provide different measurement capabilities.
    """

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    GetMetadata: grpc.UnaryUnaryMultiCallable[
        ni_measurementlink_measurement_v1_measurement_service_pb2.GetMetadataRequest,
        ni_measurementlink_measurement_v1_measurement_service_pb2.GetMetadataResponse,
    ]
    """Returns information that describes the measurement."""

    Measure: grpc.UnaryUnaryMultiCallable[
        ni_measurementlink_measurement_v1_measurement_service_pb2.MeasureRequest,
        ni_measurementlink_measurement_v1_measurement_service_pb2.MeasureResponse,
    ]
    """API used to perform a measurement."""

class MeasurementServiceAsyncStub:
    """Service that implements a measurement. Unlike other services, a MeasurementService is designed to be a plugin
    where there can be multiple implementations of the service that provide different measurement capabilities.
    """

    GetMetadata: grpc.aio.UnaryUnaryMultiCallable[
        ni_measurementlink_measurement_v1_measurement_service_pb2.GetMetadataRequest,
        ni_measurementlink_measurement_v1_measurement_service_pb2.GetMetadataResponse,
    ]
    """Returns information that describes the measurement."""

    Measure: grpc.aio.UnaryUnaryMultiCallable[
        ni_measurementlink_measurement_v1_measurement_service_pb2.MeasureRequest,
        ni_measurementlink_measurement_v1_measurement_service_pb2.MeasureResponse,
    ]
    """API used to perform a measurement."""

class MeasurementServiceServicer(metaclass=abc.ABCMeta):
    """Service that implements a measurement. Unlike other services, a MeasurementService is designed to be a plugin
    where there can be multiple implementations of the service that provide different measurement capabilities.
    """

    @abc.abstractmethod
    def GetMetadata(
        self,
        request: ni_measurementlink_measurement_v1_measurement_service_pb2.GetMetadataRequest,
        context: _ServicerContext,
    ) -> typing.Union[ni_measurementlink_measurement_v1_measurement_service_pb2.GetMetadataResponse, collections.abc.Awaitable[ni_measurementlink_measurement_v1_measurement_service_pb2.GetMetadataResponse]]:
        """Returns information that describes the measurement."""

    @abc.abstractmethod
    def Measure(
        self,
        request: ni_measurementlink_measurement_v1_measurement_service_pb2.MeasureRequest,
        context: _ServicerContext,
    ) -> typing.Union[ni_measurementlink_measurement_v1_measurement_service_pb2.MeasureResponse, collections.abc.Awaitable[ni_measurementlink_measurement_v1_measurement_service_pb2.MeasureResponse]]:
        """API used to perform a measurement."""

def add_MeasurementServiceServicer_to_server(servicer: MeasurementServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...