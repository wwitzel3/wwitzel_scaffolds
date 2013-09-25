<html>
<body>

<p>Welcome back, ${username}!</p>

<p>If you are viewing this page, it means you have 'entry' access.</p>

<p><a href="${request.route_url('example_index')}">Click here</a> to access the simple form example.</p>

<p><a href="${request.route_url('core', action='admin')}">Click here</a> for admin access (authorized users only)</p>

<p><a href="${request.route_url('core', action='logout')}">Click here</a> to logout.</p>

</body>
</html>
