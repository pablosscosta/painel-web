{% extends "base.html" %}

{% block title %}{{ titulo }}{% endblock %}

{% block content %}
<h1>ℹ️ Sobre o Sistema</h1>
<p>Sistema de monitoramento industrial desenvolvido para transformar dados de arquivos em dashboards em tempo real.</p>
<p><strong>Versão:</strong> 1.0</p>
<p><strong>Autor:</strong> Pablo Sousa da Costa</p>
<a href="{{ url_for('home') }}" class="btn">← Voltar</a>
{% endblock %}