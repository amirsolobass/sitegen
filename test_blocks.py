from src.markdown_block import markdown_to_blocks, block_to_block_type

text = """Basic chords:

```bash
$ python3 src/main.py "C"
Chord: C
Notes: C E G
```"""

blocks = markdown_to_blocks(text)
print(f"Number of blocks: {len(blocks)}")
for i, block in enumerate(blocks):
    block_type = block_to_block_type(block)
    print(f"\nBlock {i} (type: {block_type}):")
    print(repr(block[:80]))
