from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
	s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')
        s5 = self.addSwitch('s5')
        s6 = self.addSwitch('s6')
        s7 = self.addSwitch('s7')
        s8 = self.addSwitch('s8')
        s9 = self.addSwitch('s9')

	h1 = self.addHost('h1', ip='10.0.0.1/24', mac='00:00:00:00:00:01')
        h2 = self.addHost('h2', ip='10.0.0.2/24', mac='00:00:00:00:00:02')
        h3 = self.addHost('h3', ip='10.0.0.3/24', mac='00:00:00:00:00:03')
        h4 = self.addHost('h4', ip='10.0.0.4/24', mac='00:00:00:00:00:04')
        h5 = self.addHost('h5', ip='10.0.0.5/24', mac='00:00:00:00:00:05')
        h6 = self.addHost('h6', ip='10.0.0.6/24', mac='00:00:00:00:00:06')
        h7 = self.addHost('h7', ip='10.0.0.7/24', mac='00:00:00:00:00:07')
        h8 = self.addHost('h8', ip='10.0.0.8/24', mac='00:00:00:00:00:08')
        h9 = self.addHost('h9', ip='10.0.0.9/24', mac='00:00:00:00:00:09')


        # Add links
	self.addLink(s1, h1)
        self.addLink(s2, h2)
        self.addLink(s3, h3)
        self.addLink(s4, h4)
        self.addLink(s5, h5)
        self.addLink(s6, h6)
        self.addLink(s7, h7)
        self.addLink(s8, h8)
        self.addLink(s9, h9)
        #adding links switch to switch
        self.addLink(s1, s2)
        self.addLink(s1, s3)
        self.addLink(s1, s8)
        self.addLink(s1, s9)
        self.addLink(s2, s3)
        self.addLink(s2, s4)
        self.addLink(s2, s9)
        self.addLink(s3, s4)
        self.addLink(s3, s5)
        self.addLink(s4, s5)
        self.addLink(s4, s6)
        self.addLink(s5, s6)
        self.addLink(s5, s7)
        self.addLink(s6, s7)
        self.addLink(s6, s8)
        self.addLink(s7, s8)
        self.addLink(s7, s9)
        self.addLink(s8, s9)
        import pdb;pdb.set_trace()
	#reciver
        h1.cmd('./ditg/bin/ITGRecv -l rec_custom_log1 &')
        h2.cmd('./ditg/bin/ITGRecv -l rec_custom_log2 &')
        h3.cmd('./ditg/bin/ITGRecv -l rec_custom_log3 &')
        h4.cmd('./ditg/bin/ITGRecv -l rec_custom_log4 &')
        h5.cmd('./ditg/bin/ITGRecv -l rec_custom_log5 &')
        h6.cmd('./ditg/bin/ITGRecv -l rec_custom_log6 &')
        h7.cmd('./ditg/bin/ITGRecv -l rec_custom_log7 &')
        h8.cmd('./ditg/bin/ITGRecv -l rec_custom_log8 &')
        h9.cmd('./ditg/bin/ITGRecv -l rec_custom_log9 &')
        #sender
        h1.cmd('./ditg/bin/ITGSend ./script_file_custom &')
        h2.cmd('./ditg/bin/ITGSend ./script_file_custom &')
        h3.cmd('./ditg/bin/ITGSend ./script_file_custom &')
        h4.cmd('./ditg/bin/ITGSend ./script_file_custom &')
        h5.cmd('./ditg/bin/ITGSend ./script_file_custom &')
        h6.cmd('./ditg/bin/ITGSend ./script_file_custom &')
        h7.cmd('./ditg/bin/ITGSend ./script_file_custom &')
        h8.cmd('./ditg/bin/ITGSend ./script_file_custom &')
        h9.cmd('./ditg/bin/ITGSend ./script_file_custom &')


topos = { 'mytopo': ( lambda: MyTopo() )}
