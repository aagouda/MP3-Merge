
	use MP3::Merge;

	$mp = MP3::Merge->new();
	$mp->add('C:\00\audio\001006.mp3', 'C:\00\audio\001007.mp3');
	$mp->save('C:\00\audio\saved.mp3');

