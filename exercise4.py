'''
1. The creator of the database was sloppy and accidentally entered some movies twice. How can you find out which? Remove them from the database! Make sure to also remove the dependent foreign key constraints from other tables.
    select * from movie m inner join (select title, count(*) as dupeCount from movie group by title having count(*) > 1) dup on m.title = dup.title;
2. How many of the movies you crawled in the first exercise are already in the IMDB db? Which are missing?
-
3. How many of the actors you crawled in the first exercise are already in the IMDB db? Do you notice a problem?
-
4. What is the most frequently occurring movie keyword?
    select keyword, count(*) as anzahl from keyword k left join movie_keyword mk on k.id = mk.keyword_id group by k.keyword order by anzahl desc limit 25;
    murder (2751)
5. Choose 5 keywords and find out how many movies match with each.
    select keyword, count(*) as anzahl from keyword k left join movie_keyword mk on k.id = mk.keyword_id group by k.keyword order by anzahl desc limit 25;
6. Display the top 5 most frequent movie keywords and how often they occur.
    select keyword, count(*) as anzahl from keyword k left join movie_keyword mk on k.id = mk.keyword_id group by k.keyword order by anzahl desc limit 5;
7. List all directors who have produced more than 10 movies yet still retain an average tomatometer score of over 90% over all their movies combined.
    select count(*) as movie_count, avg(movie.tomatometer) as avg_tomatometer, person.name from role_type rl inner join cast_info ci on rl.id = ci.role_id right join person on person.id = ci.person_id right join movie on movie.id = ci.movie_id where rl.role = 'director' group by person.name having movie_count > 10 and avg_tomatometer > 90 limit 25;
8. List all movies that reference 'The Matrix'?
    select * from movie join movie_link on movie.id = movie_link.movie_id join movie m on m.id = movie_link.linked_movie_id where m.title like 'The Matrix%' limit 25;
9. List all the keywords that describe 'The Matrix'.
    select * from movie m inner join movie_keyword mk on m.id = mk.movie_id inner join keyword k on mk.keyword_id = k.id where m.title like 'The Matrix%' limit 25;
10. Which keywords do the movies 'The Matrix' and 'The Matrix Reloaded' have in common?
    select * from (select k.keyword from movie m inner join movie_keyword mk on m.id = mk.movie_id inner join keyword k on mk.keyword_id = k.id where m.title like 'The Matrix') m where keyword in (select k.keyword from movie m inner join movie_keyword mk on m.id = mk.movie_id inner join keyword k on mk.keyword_id = k.id where m.title like 'The Matrix Reloaded') limit 25;
11. List all actors who appear in 'The Matrix' along with the total number of movies they appear in including the tomatometer score.
12. Which actor or actress who starred in at least 3 movies since 2000 has the overall best or worst average tomatometer?
13. List all occurring tomatometer values, how many times they're seen in the movie table and calculate the percentage of occurrence with respect to all table rows.
'''