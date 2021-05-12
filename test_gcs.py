import fsspec
import xarray
import dask.array


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
