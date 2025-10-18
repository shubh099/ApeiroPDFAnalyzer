import camelot

# Test camelot on first 3 pages
pdf_path = 'uploads/90301fbb-a563-4a19-81cf-d4811a4c26e1.pdf'

print("Testing Camelot PDF extraction on first 3 pages...")
print("=" * 80)

# Try 'stream' flavor first (better for tables without clear borders)
tables = camelot.read_pdf(pdf_path, pages='1-3', flavor='stream')

print(f"\nFound {len(tables)} tables\n")

for i, table in enumerate(tables):
    print(f"Table {i+1}:")
    print(f"  Page: {table.page}")
    print(f"  Shape: {table.df.shape}")  # (rows, columns)
    print(f"  Columns: {list(table.df.columns)}")
    print(f"\nFirst 10 rows:")
    print(table.df.head(10))
    print("\n" + "="*80 + "\n")

print("\nSUCCESS CRITERIA CHECK:")
print("=" * 80)
if tables:
    first_table = tables[0]
    num_cols = first_table.df.shape[1]
    num_rows = first_table.df.shape[0]

    print(f"✓ Number of tables found: {len(tables)}")
    print(f"✓ First table columns: {num_cols} (expecting ~4, not 11)")
    print(f"✓ First table rows: {num_rows} (expecting 10+)")

    # Check if text is fragmented
    sample_text = str(first_table.df.iloc[0, 0]) if num_rows > 0 else ""
    print(f"✓ Sample text from first cell: '{sample_text[:50]}...'")

    if num_cols == 4 and num_rows >= 10:
        print("\n✅ SUCCESS! Camelot extraction looks good!")
    else:
        print(f"\n⚠️  WARNING: Table structure may need adjustment")
        print(f"   Expected 4 columns, got {num_cols}")
        print(f"   Expected 10+ rows, got {num_rows}")
else:
    print("❌ FAILED: No tables found")
