# -*- coding:utf-8 -*-
# @FileName : slice.py
# @Time : 2024/1/30 9:24
# @Author :fiv

from functools import partial
from multiprocessing.pool import ThreadPool
from pathlib import Path
from typing import Tuple

from pydub import AudioSegment
from pydub.utils import make_chunks

from env import SLICE_PATH, NUM_PROCESSES


def save(chunks: Tuple[int, AudioSegment], out_dir: Path) -> None:
    index, chunk = chunks
    chunk_name: Path = out_dir / f"{index:02d}.wav"
    chunk.export(chunk_name, format="wav")


def slice_wav(wave_path: Path, slice_step: int = 30000) -> None:
    audio = AudioSegment.from_file(wave_path, "wav")
    out_dir = SLICE_PATH / wave_path.stem
    out_dir.mkdir(parents=True, exist_ok=True)
    chunks = make_chunks(audio, slice_step)
    chunks = list(zip(range(len(chunks)), chunks))
    save_p = partial(save, out_dir=out_dir)

    with ThreadPool(NUM_PROCESSES) as pool:
        pool.map(save_p, chunks)
