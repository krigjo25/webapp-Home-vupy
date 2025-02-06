{% with flash = get_flashed_messages()%}
{% for i in flash %}
<div class="flash">{{ i }}</div>
{% endfor %}
{% endwith %}
<section id="specialization-container" class="spec-wrapper"></section> 