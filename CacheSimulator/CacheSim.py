import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

class Cache:
    def __init__(self, cache_size, block_size, mapping_technique):
        self.cache_size = cache_size
        self.block_size = block_size
        self.mapping_technique = mapping_technique
        if mapping_technique == "direct":
            self.num_blocks = cache_size // block_size
            self.cache = [-1] * self.num_blocks
        elif mapping_technique == "set associative":
            self.num_sets = cache_size // (block_size * 2)  # Assuming 2-way set associative
            self.cache = [[-1] * 2 for _ in range(self.num_sets)]  # 2-way set associative cache
        elif mapping_technique == "associative":
            self.cache = {}  # Associative cache using a dictionary
        else:
            raise ValueError("Invalid cache mapping technique")
        self.hits = 0
        self.misses = 0
        self.evictions = 0

    def access(self, address):
        tag, index = self.get_tag_and_index(address)
        if self.mapping_technique == "direct":
            if self.cache[index] == tag:
                self.hits += 1
                output_text.insert(tk.END, f"Cache hit for address {address}\n")
            else:
                self.misses += 1
                if self.cache[index] != -1:
                    self.evictions += 1
                    output_text.insert(tk.END, f"Cache eviction for address {address}\n")
                self.cache[index] = tag
                output_text.insert(tk.END, f"Cache miss for address {address}, block {index} updated with tag {tag}\n")
        elif self.mapping_technique == "set associative":
            set_index = index % self.num_sets
            if tag in self.cache[set_index]:
                self.hits += 1
                output_text.insert(tk.END, f"Cache hit for address {address}\n")
            else:
                self.misses += 1
                if -1 in self.cache[set_index]:
                    self.cache[set_index][self.cache[set_index].index(-1)] = tag
                    output_text.insert(tk.END, f"Cache miss for address {address}, tag {tag} added to set {set_index}\n")
                else:
                    self.evictions += 1
                    output_text.insert(tk.END, f"Cache eviction for address {address}\n")
                    self.cache[set_index][0] = tag  # Replace the first block in the set
                    output_text.insert(tk.END, f"Cache miss for address {address}, tag {tag} added to set {set_index}\n")
        elif self.mapping_technique == "associative":
            if tag in self.cache:
                self.hits += 1
                output_text.insert(tk.END, f"Cache hit for address {address}\n")
            else:
                self.misses += 1
                if len(self.cache) < self.cache_size // self.block_size:
                    self.cache[tag] = index
                    output_text.insert(tk.END, f"Cache miss for address {address}, tag {tag} added\n")
                else:
                    self.evictions += 1
                    output_text.insert(tk.END, f"Cache eviction for address {address}\n")
                    removed_tag = next(iter(self.cache))
                    del self.cache[removed_tag]
                    self.cache[tag] = index
                    output_text.insert(tk.END, f"Cache miss for address {address}, tag {tag} added\n")
        else:
            raise ValueError("Invalid cache mapping technique")

    def get_tag_and_index(self, address):
        binary_address = bin(address)[2:].zfill(32)
        tag_bits = binary_address[:-int(self.cache_size.bit_length() - self.block_size.bit_length())]
        index_bits = binary_address[-int(self.cache_size.bit_length() - self.block_size.bit_length()):]
        return tag_bits, int(index_bits, 2)


def simulate():
    output_text.delete(1.0, tk.END)  # Clear previous output
    main_memory_capacity = int(entry_main_memory.get())
    cache_capacity = int(entry_cache_memory.get())
    block_size = int(entry_block_size.get())
    mapping_technique = combobox_mapping_technique.get().lower()
    memory_trace = list(map(int, entry_memory_trace.get().split()))
    
    cache = Cache(cache_capacity, block_size, mapping_technique)
    for address in memory_trace:
        cache.access(address)
    
    output_text.insert(tk.END, f"Cache Hits: {cache.hits}\n")
    output_text.insert(tk.END, f"Cache Misses: {cache.misses}\n")
    output_text.insert(tk.END, f"Cache Evictions: {cache.evictions}\n")


root = tk.Tk()
root.title("Cache Simulation")

# Main memory capacity
label_main_memory = ttk.Label(root, text="Main Memory Capacity (bytes):")
label_main_memory.grid(row=0, column=0, padx=5, pady=5, sticky="w")
entry_main_memory = ttk.Entry(root, width=15)
entry_main_memory.grid(row=0, column=1, padx=5, pady=5)

# Cache memory capacity
label_cache_memory = ttk.Label(root, text="Cache Memory Capacity (bytes):")
label_cache_memory.grid(row=1, column=0, padx=5, pady=5, sticky="w")
entry_cache_memory = ttk.Entry(root, width=15)
entry_cache_memory.grid(row=1, column=1, padx=5, pady=5)

# Block size
label_block_size = ttk.Label(root, text="Block Size (bytes):")
label_block_size.grid(row=2, column=0, padx=5, pady=5, sticky="w")
entry_block_size = ttk.Entry(root, width=15)
entry_block_size.grid(row=2, column=1, padx=5, pady=5)

# Mapping technique
label_mapping_technique = ttk.Label(root, text="Mapping Technique:")
label_mapping_technique.grid(row=3, column=0, padx=5, pady=5, sticky="w")
combobox_mapping_technique = ttk.Combobox(root, values=["Direct", "Set Associative", "Associative"], width=15)
combobox_mapping_technique.grid(row=3, column=1, padx=5, pady=5)
combobox_mapping_technique.current(0)

# Memory trace
label_memory_trace = ttk.Label(root, text="Memory Trace (addresses separated by space):")
label_memory_trace.grid(row=4, column=0, padx=5, pady=5, sticky="w")
entry_memory_trace = ttk.Entry(root, width=50)
entry_memory_trace.grid(row=4, column=1, padx=5, pady=5)

# Button to start simulation
button_simulate = ttk.Button(root, text="Simulate", command=simulate)
button_simulate.grid(row=5, column=1, padx=5, pady=5, sticky="e")

# Output text widget
output_text = scrolledtext.ScrolledText(root, width=70, height=15, wrap=tk.WORD)
output_text.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()