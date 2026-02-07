import inspect

from augur.tasks.start_tasks import (
    CollectionRequestBuilder,
    PrimaryCollectionRequestBuilder,
    SecondaryCollectionRequestBuilder,
    FacadeCollectionRequestBuilder,
    MLCollectionRequestBuilder,
    build_primary_repo_collect_request,
    build_secondary_repo_collect_request,
    build_facade_repo_collect_request,
    build_ml_repo_collect_request,
)


def test_builders_are_subclasses():
    assert issubclass(PrimaryCollectionRequestBuilder, CollectionRequestBuilder)
    assert issubclass(SecondaryCollectionRequestBuilder, CollectionRequestBuilder)
    assert issubclass(FacadeCollectionRequestBuilder, CollectionRequestBuilder)
    assert issubclass(MLCollectionRequestBuilder, CollectionRequestBuilder)


def test_builders_have_build_method():
    for cls in (
        PrimaryCollectionRequestBuilder,
        SecondaryCollectionRequestBuilder,
        FacadeCollectionRequestBuilder,
        MLCollectionRequestBuilder,
    ):
        assert hasattr(cls, "build")
        assert inspect.isfunction(cls.build) or inspect.ismethod(cls.build)


def test_wrapper_functions_exist():
    assert callable(build_primary_repo_collect_request)
    assert callable(build_secondary_repo_collect_request)
    assert callable(build_facade_repo_collect_request)
    assert callable(build_ml_repo_collect_request)


def test_build_method_signature_contains_expected_params():
    # Ensure builders accept enabled phase names
    for cls in (
        PrimaryCollectionRequestBuilder,
        SecondaryCollectionRequestBuilder,
        FacadeCollectionRequestBuilder,
        MLCollectionRequestBuilder,
    ):
        sig = inspect.signature(cls.build)
        params = list(sig.parameters.keys())
        assert "enabled_phase_names" in params
        assert "days_until_collect_again" in params


def test_wrapper_signatures_match_build():
    # Wrappers should match builder params
    builders_and_wrappers = [
        (PrimaryCollectionRequestBuilder, build_primary_repo_collect_request),
        (SecondaryCollectionRequestBuilder, build_secondary_repo_collect_request),
        (FacadeCollectionRequestBuilder, build_facade_repo_collect_request),
        (MLCollectionRequestBuilder, build_ml_repo_collect_request),
    ]

    for builder_cls, wrapper in builders_and_wrappers:
        builder_sig = inspect.signature(builder_cls.build)
        wrapper_sig = inspect.signature(wrapper)
        # Ignore 'self' when comparing
        builder_params = [p for p in list(builder_sig.parameters.keys()) if p != 'self']
        wrapper_params = list(wrapper_sig.parameters.keys())
        assert builder_params == wrapper_params



