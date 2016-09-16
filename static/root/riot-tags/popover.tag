<popover-component>
	<a href="" name='popTag'>{ opts.text }</a>
<script>
	$(this.popTag).webuiPopover({
		title:opts.title,
		trigger:'hover',
		width: 900,
		height: 500,
		closable: true,
		animation: 'pop',
		type:'iframe',url:opts.url
	});
</script>

</popover-component>