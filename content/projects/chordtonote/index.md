# ChordToNote

A simple command-line tool to convert chord names to their constituent notes. Perfect for musicians, students, and developers learning music theory.

## Features

- **Wide Chord Support** - Handles major, minor, seventh, ninth, eleventh, thirteenth chords, augmented, diminished, suspended, and power chords
- **Accidentals** - Supports sharps (#) and flats (b) in root notes
- **Slash Chords** - Includes bass notes
- **Case Insensitive** - Accepts chords in any case
- **Enharmonic Equivalents** - Automatically selects appropriate note names based on chord type
- **No Dependencies** - Pure Python implementation with no external requirements

## Installation

1. Clone or download the project:
   ```bash
   cd chordtonote
   ```

2. Ensure Python 3.8+ is installed

3. No external dependencies required!

## Usage

```
python3 src/main.py YOUR_CHORD_HERE
```

### Examples

Basic chords:

```bash
$ python3 src/main.py "C"
Chord: C
Notes: C E G

$ python3 src/main.py "Cm"
Chord: Cm
Notes: C Eb G
```

Seventh chords:

```bash
$ python3 src/main.py "C7"
Chord: C7
Notes: C E G Bb

$ python3 src/main.py "Cm7"
Chord: Cm7
Notes: C Eb G Bb
```

Sharp/flat roots:

```bash
$ python3 src/main.py "F#"
Chord: F#
Notes: F# A# C#

$ python3 src/main.py "Bb"
Chord: Bb
Notes: Bb D F
```

Slash chords:

```bash
$ python3 src/main.py "Gm/E"
Chord: Gminor/E
Notes: E G Bb D
```

Case insensitive:

```bash
$ python3 src/main.py "bdIm"
Chord: bdim
Notes: B D F
```

## Supported Chords

Triads: major, minor, dim, aug, sus2, sus4, 5 (power)

Seventh Chords: maj7, m7, 7, m7b5, dim7, aug7, augmaj7, mmaj7, 7sus4, 7sus2

Extended Chords: maj9, m9, 9, m9b5, aug9, augmaj9, mmaj9

Eleventh and Thirteenth: maj11, m11, 11, m11b5, aug11, augmaj11, mmaj11, maj13, m13, 13, m13b5, aug13, augmaj13, mmaj13

## Project Structure

- src/main.py - Main entry point
- src/note_calc.py - Note calculation logic
- src/scales.py - Scale and chord interval definitions
- src/interval_maps.py - Music interval mappings
- src/root_extraction.py - Chord parsing and root extraction
- src/test_chordtonote.py - Test suite

## Development

Run tests:
```bash
python3 src/test_chordtonote.py
```

## Requirements

- Python 3.8+
- No external dependencies

## Music Theory Background

This tool is based on standard music theory:
- Each chord consists of a root note plus intervals
- Sharps and flats adjust note names
- Slash chords add a specific bass note
- Enharmonic equivalents are handled intelligently

## Contributing

Feel free to open issues or submit pull requests for new features or bug fixes.

## Use Cases

- Learning music theory
- Chord-to-scale suggestions
- Music software development
- Educational tools
- Musicians' practice companion
