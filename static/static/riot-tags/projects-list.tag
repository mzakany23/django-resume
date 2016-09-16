<projects-list>
	<ul id="project" class='display-big'>
		<li each={ project in projects }>
			<a onclick={ showPopup } href='#{ project.href || project.title }'  data-toggle="modal" data-target="#projectModal">
				<img src="{ MEDIA_URL }{ project.thumbnail }">
			</a>
		</li>
	</ul>

	<modal project={ currentProject }></modal>

	<script>
		var self = this
		var currentProject = null

		this.on('mount',function() {
			$.get(location.origin + '/api/projects').then(function(projects) {
				self.projects = projects
				self.update()
			})
		})

		this.showPopup = function(e) {
			var project = e.item.project
			self.currentProject = project
		}
	</script>
</projects-list>