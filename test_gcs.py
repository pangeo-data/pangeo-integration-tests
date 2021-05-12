import fsspec
import xarray
import dask.array
import asyncio
import gcsfs


def test_write_zarr(tmp_gcs_path):
    ds = xarray.Dataset(
        {
            "a": (
                ["x", "y", "z"],
                dask.array.ones(shape=(100, 100, 100), chunks=(10, 10, 10)),
            )
        }
    )
    mapper = fsspec.get_mapper(tmp_gcs_path)
    ds.to_zarr(mapper)


def test_write_quickly_to_object_in_parallel(tmp_gcs_path):
    """Google has an api limit for writing to an object of 1/sec

    This is a potent test of gcsfs' retry logic for writes
    """
    loop = asyncio.get_event_loop()
    fs = gcsfs.GCSFileSystem(asynchronous=True, loop=None)

    data = b"hello world"

    writes = asyncio.gather(*[fs._pipe_file(tmp_gcs_path, data) for _ in range(40)])
    loop.run_until_complete(writes)

    fs = gcsfs.GCSFileSystem()
    assert fs.cat(tmp_gcs_path) == data
