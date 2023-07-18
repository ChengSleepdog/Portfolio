from rest_framework import serializers

class ScanParameterSerializer(serializers.Serializer):
    scan_mod = serializers.CharField(
        required=False,
        default='default',
        help_text='e.g. `custom`, `default`, `host_discover`')
    scan_host_range = serializers.ListSerializer(child=serializers.CharField(
        help_text='e.g. [10.40.192.0/26, 10.40.192-195.10-100,  10.40.192.230-240,245-250]'))  # list
    scan_host_port = serializers.CharField(
        allow_blank=True,
        required=False,
        default="1-1024",
        help_text='e.g. 80,443 or 1-65535')
    scan_host_exclude = serializers.CharField(
        allow_blank=True,
        required=False,
        default='',
        help_text='e.g. 10.40.192.184')
    scan_speed = serializers.CharField(
        required=False,
        default='T3',
        help_text='e.g. `T1`~`T5`')
    scan_delay = serializers.CharField(
        allow_blank=True,
        required=False,
        default='0ms',
        help_text='e.g. 500ms , 2s , 1m')
    scan_host_timeout = serializers.CharField(
        allow_blank=True,
        required=False, default='500ms', help_text='e.g. 500ms , 2s , 1m')
    scan_args = serializers.CharField(
        allow_blank=True,
        required=False,
        default='',
        help_text='[https://nmap.org/book/man-briefoptions.html]')
    