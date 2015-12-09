"""
This example shows how to create an empty Mininet object
(without a topology object) and add nodes to it manually.
"""

from mininet.net import Mininet
from mininet.net import Node
from mininet.net import Link
from mininet.node import Controller, RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def net_br0_port1():

    info( '*** Adding controller\n')
    CONTROLLER_IP= '192.168.70.95:6644'

    net=Mininet( topo=None, build=False)

    info( '*** Adding hosts\n')
    net1 = net.addHost( 'net1')
    net2 = net.addHost( 'net2')


    info( '*** Adding switch\n')
    br0 = net.addSwitch( 'br0')



    info( '*** Creating links\n' )
    net.addLink( net1, br0 )
    net.addLink( net2, br0 )



    info( '*** Starting network and add bridge \n' )




    controller = net.addController('c0', controller=RemoteController, ip=CONTROLLER_IP, Port=6633)

    info( '*** Starting network\n')
    net.start()

    br0.cmd('ovs-vsctl add-port br0 port1')

    info( '*** Running CLI\n' )
    CLI( net )

    info( '*** Stopping network' )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    net_br0_port1()