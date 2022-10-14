# Healthify Me

The program reminds you to drink water, do some physical exercise and make some eye movement after regular intervals of time by playing respective mp3 files. It also logs the timestamp of the activity (like drinking water, physical exercise and eye movement) performed in a `log_timestamp_file.txt` file.

The default timeouts for eye, water and exercise breaks are 1200s, 3600s and 4800s respectively.

You can change them by adding a config.json file in the same directory as of the python file, like this:

```json
{
	"eyes_timeout": 1200,
	"water_timeout": 3600,
	"exercise_timeout": 2400
}
```

You can run this program by downloading `eye.mp3`, `exercise.mp3` , `water.mp3` in the same directory as the `healthy_me.py` file.

This program makes you healthy by incorporating a routine of regular eye and body movements and keeping you hydrated!