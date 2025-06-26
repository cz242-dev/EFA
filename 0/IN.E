# INDEX 
~/
# Route, that points on function `step`
~/step?[from=@&to=@]
# Route, that points on function `foot`
~/foot?[from=@&to=@]!new[size=@]
# Route, that points on existing function or module->function
~/[[module]@method]?[[]@]![[module]@method#model]
