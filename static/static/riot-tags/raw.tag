<raw>
	
<script>
	var self = this
	this.updateContent = function() {
		this.root.innerHTML = opts.content
	}

	this.on('update',function() {
		this.updateContent()
	})

	this.updateContent()
</script>

</raw>