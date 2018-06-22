---
layout: default
---

<h2 class="post-list-heading">{{ page.list_title | default: "Posts" }}</h2>
{%- for post in site.posts -%}
	{% include post_card.html post=post %}
{%- endfor -%}