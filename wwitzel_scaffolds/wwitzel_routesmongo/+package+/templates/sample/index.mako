<%inherit file="../base.mako"/>

<h3>Samples</h3>
<ul>
% for sample in samples:
    <li> <a href="${request.route_url('sample', id=sample.id)}">${sample.name}</a> </li>
% endfor
</ul>