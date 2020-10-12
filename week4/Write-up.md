<b><h1>Configure default route to the routers:</h1></b><br>

<b><i>Procedure:</i></b>
<ol>
<li>Three routers are placed on the same level and connected using serial DCE cable. The three routers are named as router0, router1 and router2.</li>
<li>A switch called switch0 is placed alongside router0 and another called switch1 is placed alongside router2. The connection between routers and switches is done using copper staright-through cables.</li>
<li>Two generic computers are placed alongside each switch. For switch0 the computers are named PC0 and PC1. For switch1 computers are named PC2 and PC3.</li>
<li>IP addresses and default gateway addresses are configured seperately for all four computers.</li>
<li>The terminal of each router is accessed and the interfaces for each connection is established with specified gateway addresses.</li>
</ol><br>

<b><i>Observations:</i></b>
<ol>
<li>Pinging any destination computer from any source initially gives an error stating <i>destination host unreachable</i> because there is no direct connection between source and destination.</li>
<li>The ip route of the routers can be seen using <i>show ip route</i> command for each router.</li>
<li>In order to send ping message irrespective of destination addresses via routers we add default routes to routers router0 and router2.This can be done as follows:<br><br>
<ul>
<li>For router0:<br>
Route through 10.0.0.0 and 20.0.0.0 is directly connected. Therefore, we add default route with next hop address as 20.0.0.2.<br>
<i>Router(config)#ip route 0.0.0.0 0.0.0.0 20.0.0.2<br></i></li>
<li>For router2:<br>
Route through 30.0.0.0 and 40.0.0.0 is directly connected. Therefore, we add default route with next hop address as 30.0.0.1.<br>
<i>Router(config)#ip route 0.0.0.0 0.0.0.0 30.0.0.1<br></i></li>
</ul>
</li><br>
<li>For router1:<br>
Route through 20.0.0.0 and 30.0.0.0 is directly connected. Therefore, we add static route through 10.0.0.0 and 40.0.0.0.<br>
<i>Router(config)#ip route 10.0.0.0 255.0.0.0 20.0.0.1<br>
Router(config)#ip route 40.0.0.0 255.0.0.0 30.0.0.2</i></li>
</li>
<li>After adding default routes to routers, router0 and router2, a connection is established between each interface and pinging from any source to any destination works as per the requirement.</li>
</ol><br>

<b><i>Learning Outcomes:</i></b>
<ol>
<li>Configuring a topology with multiple routers.</li>
<li>Configuring IP and default gateway addresses for PCs.</li>
<li>Configuring IP addresses for interfaces.</li>
<li>Configuring static IP routes for ping messages to give the desired response since they give an error if there is no direct connection between device networks.</li>
<li>Configuring default IP routes to routers such that irrespective of destination address the packet is forwarded to the next hop address specified.</li>
</ol>
