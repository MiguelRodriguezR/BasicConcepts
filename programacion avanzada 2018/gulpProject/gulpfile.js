var gulp = require('gulp');
var sass = require('gulp-sass');
var uglify = require('gulp-uglify');
var connect = require('gulp-connect');
var pump = require('pump');

htmlSources = ['*.html'];

gulp.task('default', defaultTask);


function defaultTask(done) {
  // place code for your default task here
  done();
}

// Most important methods of gulp object are:
//
// src where we put the name of the file we want to work with and use as an input,
// pipe will take output of the previous command as pipe it as an input for the next,
// dest writes the output of previous commands to the folder we specify

gulp.task('copy',(done)=>{
  gulp.src('index.html')
  .pipe(gulp.dest('assets'));
  done();
});

// folder/*.html - will match all the HTML files in folder
// root/**/*.html - will match all the HTML files in all the folders from root to its children

gulp.task('sass',()=>{
  return gulp.src('styles/*.scss')
    .pipe(sass().on('error', sass.logError))
    .pipe(gulp.dest('assets'));
});

// creando un whatcher para sass

gulp.task('sass:watch', function () {
  gulp.watch('styles/*.scss', gulp.parallel('sass'));
});

gulp.task('compress', (done) => {
  pump([
        gulp.src('js/*.js'),
        uglify(),
        gulp.dest('assets')
    ],
    done
  );
});

//gulp.task('default', gulp.parallel('sass','copy'));


gulp.task('connect',()=>{
  connect.server({
   root: '.',
   livereload: true
  })
});

gulp.task('html',()=>{
  gulp.src(htmlSources)
  .pipe(connect.reload())
});

gulp.task('default', gulp.parallel('html', 'compress', 'sass', 'connect', 'sass:watch'));
