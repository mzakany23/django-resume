<modal>
	<div class="modal" id='projectModal' tabindex="-1" role="dialog">
	  <div class="modal-dialog" role="document">
	    <div class="modal-content">
	      <div class="modal-header">
	        <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
	        <h4 class="modal-title">{ project.title }</h4>
	      </div>
	      <div class="modal-body">
	      	<img class='thumbnail' width='100%' style='max-height: 400px;' src={ project.thumbnail }>
	        <raw content={ project.description }></raw>
	      </div>
	      <div class="modal-footer">
	        <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
	      </div>
	    </div><!-- /.modal-content -->
	  </div><!-- /.modal-dialog -->
	</div><!-- /.modal -->
<script>
	var self = this

	this.on('update',function() {
		self.project = opts.project
	})
</script>

</modal>