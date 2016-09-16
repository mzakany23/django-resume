var gulp = require('gulp');
var imageop = require('gulp-image-optimization');
 
gulp.task('images', function(cb) {
    gulp.src(['static/static/process-images/**/*.png','static/static/process-images/**/*.jpg','static/static/process-images/**/*.gif','static/static/process-images/**/*.jpeg']).pipe(imageop({
        optimizationLevel: 5,
        progressive: true,
        interlaced: true
    })).pipe(gulp.dest('static/static/images/')).on('end', cb).on('error', cb);
});