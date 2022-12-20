# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from ni_measurement_service._internal.stubs import session_pb2 as session__pb2


class SessionUtilitiesStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.EnumerateDevices = channel.unary_unary(
            "/nidevice_grpc.SessionUtilities/EnumerateDevices",
            request_serializer=session__pb2.EnumerateDevicesRequest.SerializeToString,
            response_deserializer=session__pb2.EnumerateDevicesResponse.FromString,
        )
        self.Reserve = channel.unary_unary(
            "/nidevice_grpc.SessionUtilities/Reserve",
            request_serializer=session__pb2.ReserveRequest.SerializeToString,
            response_deserializer=session__pb2.ReserveResponse.FromString,
        )
        self.IsReservedByClient = channel.unary_unary(
            "/nidevice_grpc.SessionUtilities/IsReservedByClient",
            request_serializer=session__pb2.IsReservedByClientRequest.SerializeToString,
            response_deserializer=session__pb2.IsReservedByClientResponse.FromString,
        )
        self.Unreserve = channel.unary_unary(
            "/nidevice_grpc.SessionUtilities/Unreserve",
            request_serializer=session__pb2.UnreserveRequest.SerializeToString,
            response_deserializer=session__pb2.UnreserveResponse.FromString,
        )
        self.ResetServer = channel.unary_unary(
            "/nidevice_grpc.SessionUtilities/ResetServer",
            request_serializer=session__pb2.ResetServerRequest.SerializeToString,
            response_deserializer=session__pb2.ResetServerResponse.FromString,
        )


class SessionUtilitiesServicer(object):
    """Missing associated documentation comment in .proto file."""

    def EnumerateDevices(self, request, context):
        """Provides a list of devices or chassis connected to server under localhost"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Reserve(self, request, context):
        """Reserve a set of client defined resources for exclusive use"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def IsReservedByClient(self, request, context):
        """Determines if a set of client defined resources is currently reserved by a
        specific client
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Unreserve(self, request, context):
        """Unreserves a previously reserved resource"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ResetServer(self, request, context):
        """Resets the server to a default state with no open sessions"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_SessionUtilitiesServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "EnumerateDevices": grpc.unary_unary_rpc_method_handler(
            servicer.EnumerateDevices,
            request_deserializer=session__pb2.EnumerateDevicesRequest.FromString,
            response_serializer=session__pb2.EnumerateDevicesResponse.SerializeToString,
        ),
        "Reserve": grpc.unary_unary_rpc_method_handler(
            servicer.Reserve,
            request_deserializer=session__pb2.ReserveRequest.FromString,
            response_serializer=session__pb2.ReserveResponse.SerializeToString,
        ),
        "IsReservedByClient": grpc.unary_unary_rpc_method_handler(
            servicer.IsReservedByClient,
            request_deserializer=session__pb2.IsReservedByClientRequest.FromString,
            response_serializer=session__pb2.IsReservedByClientResponse.SerializeToString,
        ),
        "Unreserve": grpc.unary_unary_rpc_method_handler(
            servicer.Unreserve,
            request_deserializer=session__pb2.UnreserveRequest.FromString,
            response_serializer=session__pb2.UnreserveResponse.SerializeToString,
        ),
        "ResetServer": grpc.unary_unary_rpc_method_handler(
            servicer.ResetServer,
            request_deserializer=session__pb2.ResetServerRequest.FromString,
            response_serializer=session__pb2.ResetServerResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "nidevice_grpc.SessionUtilities", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class SessionUtilities(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def EnumerateDevices(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/nidevice_grpc.SessionUtilities/EnumerateDevices",
            session__pb2.EnumerateDevicesRequest.SerializeToString,
            session__pb2.EnumerateDevicesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def Reserve(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/nidevice_grpc.SessionUtilities/Reserve",
            session__pb2.ReserveRequest.SerializeToString,
            session__pb2.ReserveResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def IsReservedByClient(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/nidevice_grpc.SessionUtilities/IsReservedByClient",
            session__pb2.IsReservedByClientRequest.SerializeToString,
            session__pb2.IsReservedByClientResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def Unreserve(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/nidevice_grpc.SessionUtilities/Unreserve",
            session__pb2.UnreserveRequest.SerializeToString,
            session__pb2.UnreserveResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def ResetServer(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/nidevice_grpc.SessionUtilities/ResetServer",
            session__pb2.ResetServerRequest.SerializeToString,
            session__pb2.ResetServerResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
