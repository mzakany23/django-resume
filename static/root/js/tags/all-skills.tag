<all-skills>
<div class="box">
  <h2>Skills</h2>
  	<div class="skills">
  			
	  		<div each={ skill in data } class="item-skills" data-percent="{ skill.percent }"><a href="{ skill.link }" style="color: #ffffff">{{ skill.name }}</a></div>	

  	</div>

  	<div class="skills-legend clearfix">
      <div class="legend-left legend">Beginner</div>
      <div class="legend-left legend"><span>Proficient</span></div>
      <div class="legend-right legend"><span>Expert</span></div>
    </div>
</div>


<script>
	this.data = opts.data
	
</script>
</all-skills>