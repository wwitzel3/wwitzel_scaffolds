<html>
<body>

<form name="login_form" method="POST" action="${request.route_url('core', action='login')}">
  <label>Login:</label>
  <input type="text" name="username" value="${username}" /><br />
  <label>Password:</label>
  <input type="password" name="password" value="" /> <br />
  <input type="submit" name="submit" value="Login" />
</form>

<p>user1 / password (entry)</p>
<p>user2 / password (admin)</p>

%if failed_attempt:
<p>Login failed. Invalid username and/or password or both.</p>
%endif

</body>
</html>
