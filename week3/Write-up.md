<b><h1>Configure multiple routers and send ping messages:</h1></b><br>

<b><i>Procedure:</i></b>
<ol>
<li>Three routers are placed on the same level and connected using serial DCE cable. The three routers are named as router0, router1 and router2.</li>
<li>One generic computer is placed alongside router0 and another is placed alongside router2. The connection between routers and computers is done using copper cross-over cables.</li>
<li>IP addresses and default gateway addresses are configured seperately for both computers.</li>
<li>The terminal of each router is accessed and the interfaces for each connection is established with specified gateway addresses.</li>
</ol><br>

<b><i>Observations:</i></b>
<ol>
<li>Pinging the second computer i.e, PC1 from PC0 initially gives an error stating <i>destination host unreachable</i> because there is no direct connection between source (PC0) and destination (PC1).</li>
<li>The ip route of the routers can be seen using <i>show ip route</i> command for each router.</li>
<li>In order to send ping message to PC1 via router0, router1, we need to add static routes to routers.This can be done using the following syntax:<br>
<i>ip route <dest_network> <subnet_mask> <next_hop></i> in configure mode.<br><br>
<ul>
<li>For router0:<br>
Route through 10.0.0.0 and 20.0.0.0 is directly connected. Therefore we add static route through 30.0.0.0 and 40.0.0.0.<br>
<i>Router(config)#ip route 30.0.0.0 255.0.0.0 20.0.0.2<br>
Router(config)#ip route 40.0.0.0 255.0.0.0 20.0.0.2</i></li>
<li>For router1:<br>
Route through 20.0.0.0 and 30.0.0.0 is directly connected. Therefore we add static route through 10.0.0.0 and 40.0.0.0.<br>
<i>Router(config)#ip route 10.0.0.0 255.0.0.0 20.0.0.1<br>
Router(config)#ip route 40.0.0.0 255.0.0.0 30.0.0.2</i></li>
<li>For router2:<br>
Route through 30.0.0.0 and 40.0.0.0 is directly connected. Therefore we add static route through 10.0.0.0 and 20.0.0.0.<br>
<i>Router(config)#ip route 10.0.0.0 255.0.0.0 30.0.0.1<br>
Router(config)#ip route 20.0.0.0 255.0.0.0 30.0.0.1</i><br></li>
</ul>
</li>
<li>After adding static routes to routers, a connection is established between each interface and pinging PC1 from PC0 works as per the requirement.</li>
</ol><br>

<b><i>Learning Outcomes:</i></b>
<ol>
<li>Configuring a topology with multiple routers</li>
<li>Configuring IP and default gateway addresses for PCs</li>
<li>Configuring IP addresses for interfaces</li>
<li>Configuring static IP routes for ping messages to give the desired response since they give an error if there is no direct connection between device networks</li>
</ol>

