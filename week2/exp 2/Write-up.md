<b><h1>Configure router and send a ping message:</h1></b><br>

<b><i>Procedure:</i></b>
<ul>
<li>Router is connected with copper cross wireto two end-devices.</li>
<li>IP address and default gateway addresses are configured for each device.</li>
<li>Router's configuration terminal is accessed and connection between devices and router is established through the gateway addresses using Command Line Interface.</li>
<li>Using terminals on computer we can ping other PCs using IP address.</li>
</ul><br>

<b><i>Learning outcomes:</i></b>

To check whether packet has been received at destination end, we make use of ping command. This shows how much data has been sent, what is total round trip time, TTL etc.
Round trip time is the time taken by a packet to travel from its source to its destination and back to its source. 
TTL expanded as Time to Live gets reduced by 1 at every node. When the TTL is 0, the packet transferred is stoppped i.e, it makes sure that packet does not stay for long in the trip. There are 8 total interfaces, 1 for each PC and 4 for the router. To use ping, we need to configure router first, through the terminal and also we need to assign different default gateways to the end devices.
