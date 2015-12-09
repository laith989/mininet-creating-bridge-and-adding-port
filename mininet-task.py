"""
This example shows how to create an empty Mininet object
(without a topology object) and add nodes to it manually.
"""

from mininet.net import Mininet
from mininet.net import Node
from mininet.net import Link
from mininet.node import Controller
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def emptyNet():

    "Create an empty network and add nodes to it."

    net = Mininet( controller=Controller )

    info( '*** Adding controller\n')
    CONTROLLER_IP= '192.168.70.90'

    info( '*** Adding hosts\n')
    net1 = Node( 'net1')
    net2 = Node( 'net2')


    info( '*** Adding switch\n')
    sw1 = net.addSwitch( 'SW1')


    info( '*** Creating links\n' )
    Link( net1, sw1 )
    Link( net2, sw1 )

    sw1.cmd('ovs-vsctl del-br dp0')
    sw1.cmd('ovs-vsctl add-br br0')
    sw1.cmd('ovs-vsctl add-port port1')
    sw1.cmd('ovs-vsctl set-controller dp0 tcp:'+CONTROLLER_IP+':6633')


if __name__ == '__main__':
    setLogLevel( 'info' )
    emptyNet()