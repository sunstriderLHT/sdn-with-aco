from mininet.topo import Topo

class MyTopo( Topo ):
    

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        host1 = self.addHost('h1')
        host2 = self.addHost('h2')
        host3 = self.addHost('h3')
        host4 = self.addHost('h4')
        host5 = self.addHost('h5')
        host6 = self.addHost('h6')
        host7 = self.addHost('h7')
        host8 = self.addHost('h8')
        
        switch1 = self.addSwitch('s1')
        switch2 = self.addSwitch('s2')
        switch3 = self.addSwitch('s3')
        switch4 = self.addSwitch('s4')
        switch15 = self.addSwitch('s15')
        switch16 = self.addSwitch('s16')
        switch25 = self.addSwitch('s25')
        switch26 = self.addSwitch('s26')
        switch11 = self.addSwitch('s11')
        switch12 = self.addSwitch('s12')


        # add links
        self.addLink(host1,switch1,1,1)
        self.addLink(host2,switch1,1,2)
        self.addLink(host3,switch2,1,1)
        self.addLink(host4,switch2,1,2)
        self.addLink(host5,switch3,1,1)
        self.addLink(host6,switch3,1,2)
        self.addLink(host7,switch4,1,1)
        self.addLink(host8,switch4,1,2)
        self.addLink(switch1,switch15,3,1)
        self.addLink(switch1,switch25,4,1)
        self.addLink(switch2,switch15,3,2)
        self.addLink(switch2,switch25,4,2)
        self.addLink(switch3,switch16,3,1)
        self.addLink(switch3,switch26,4,1)
        self.addLink(switch4,switch16,3,2)
        self.addLink(switch4,switch26,4,2)
        self.addLink(switch15,switch11,3,1)
        self.addLink(switch25,switch12,3,1)
        self.addLink(switch16,switch11,3,2)
        self.addLink(switch26,switch12,3,2)



topos = { 'mytopo': ( lambda: MyTopo() ) }