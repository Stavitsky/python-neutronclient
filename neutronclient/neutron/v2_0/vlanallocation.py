from neutronclient.neutron import v2_0 as neutronV20


class ListVlanAllocations(neutronV20.ListCommand):

    """List VLANs"""
    resource = 'vlan_allocation'
    list_columns = ['vlan_id', 'physical_network', 'allocated']
    _formatters = {}
    pagination_support = False
    sorting_support = False
