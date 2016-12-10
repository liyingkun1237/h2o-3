#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# This file is auto-generated by h2o-3/h2o-bindings/bin/gen_python.py
# Copyright 2016 H2O.ai;  Apache License Version 2.0 (see LICENSE for details)
#
from __future__ import absolute_import, division, print_function, unicode_literals

from h2o.estimators.estimator_base import H2OEstimator
from h2o.exceptions import H2OValueError
from h2o.frame import H2OFrame
from h2o.utils.typechecks import assert_is_type, Enum, numeric


class H2ONaiveBayesEstimator(H2OEstimator):
    """
    Naive Bayes

    The naive Bayes classifier assumes independence between predictor variables
    conditional on the response, and a Gaussian distribution of numeric predictors with
    mean and standard deviation computed from the training dataset. When building a naive
    Bayes classifier, every row in the training dataset that contains at least one NA will
    be skipped completely. If the test dataset has missing values, then those predictors
    are omitted in the probability calculation during prediction.
    """

    algo = "naivebayes"

    def __init__(self, **kwargs):
        super(H2ONaiveBayesEstimator, self).__init__()
        self._parms = {}
        names_list = {"model_id", "nfolds", "seed", "fold_assignment", "fold_column",
                      "keep_cross_validation_predictions", "keep_cross_validation_fold_assignment", "training_frame",
                      "validation_frame", "response_column", "ignored_columns", "ignore_const_cols",
                      "score_each_iteration", "balance_classes", "class_sampling_factors", "max_after_balance_size",
                      "max_confusion_matrix_size", "max_hit_ratio_k", "laplace", "min_sdev", "eps_sdev", "min_prob",
                      "eps_prob", "compute_metrics", "max_runtime_secs"}
        if "Lambda" in kwargs: kwargs["lambda_"] = kwargs.pop("Lambda")
        for pname, pvalue in kwargs.items():
            if pname == 'model_id':
                self._id = pvalue
                self._parms["model_id"] = pvalue
            elif pname in names_list:
                # Using setattr(...) will invoke type-checking of the arguments
                setattr(self, pname, pvalue)
            else:
                raise H2OValueError("Unknown parameter %s = %r" % (pname, pvalue))

    @property
    def nfolds(self):
        """int: Number of folds for N-fold cross-validation (0 to disable or >= 2). (Default: 0)"""
        return self._parms.get("nfolds")

    @nfolds.setter
    def nfolds(self, nfolds):
        assert_is_type(nfolds, None, int)
        self._parms["nfolds"] = nfolds


    @property
    def seed(self):
        """
        int: Seed for pseudo random number generator (only used for cross-validation and fold_assignment="Random" or
        "AUTO") (Default: -1)
        """
        return self._parms.get("seed")

    @seed.setter
    def seed(self, seed):
        assert_is_type(seed, None, int)
        self._parms["seed"] = seed


    @property
    def fold_assignment(self):
        """
        Enum["auto", "random", "modulo", "stratified"]: Cross-validation fold assignment scheme, if fold_column is not
        specified. The 'Stratified' option will stratify the folds based on the response variable, for classification
        problems. (Default: "auto")
        """
        return self._parms.get("fold_assignment")

    @fold_assignment.setter
    def fold_assignment(self, fold_assignment):
        assert_is_type(fold_assignment, None, Enum("auto", "random", "modulo", "stratified"))
        self._parms["fold_assignment"] = fold_assignment


    @property
    def fold_column(self):
        """str: Column with cross-validation fold index assignment per observation."""
        return self._parms.get("fold_column")

    @fold_column.setter
    def fold_column(self, fold_column):
        assert_is_type(fold_column, None, str)
        self._parms["fold_column"] = fold_column


    @property
    def keep_cross_validation_predictions(self):
        """bool: Whether to keep the predictions of the cross-validation models. (Default: False)"""
        return self._parms.get("keep_cross_validation_predictions")

    @keep_cross_validation_predictions.setter
    def keep_cross_validation_predictions(self, keep_cross_validation_predictions):
        assert_is_type(keep_cross_validation_predictions, None, bool)
        self._parms["keep_cross_validation_predictions"] = keep_cross_validation_predictions


    @property
    def keep_cross_validation_fold_assignment(self):
        """bool: Whether to keep the cross-validation fold assignment. (Default: False)"""
        return self._parms.get("keep_cross_validation_fold_assignment")

    @keep_cross_validation_fold_assignment.setter
    def keep_cross_validation_fold_assignment(self, keep_cross_validation_fold_assignment):
        assert_is_type(keep_cross_validation_fold_assignment, None, bool)
        self._parms["keep_cross_validation_fold_assignment"] = keep_cross_validation_fold_assignment


    @property
    def training_frame(self):
        """str: Id of the training data frame (Not required, to allow initial validation of model parameters)."""
        return self._parms.get("training_frame")

    @training_frame.setter
    def training_frame(self, training_frame):
        assert_is_type(training_frame, None, H2OFrame)
        self._parms["training_frame"] = training_frame


    @property
    def validation_frame(self):
        """str: Id of the validation data frame."""
        return self._parms.get("validation_frame")

    @validation_frame.setter
    def validation_frame(self, validation_frame):
        assert_is_type(validation_frame, None, H2OFrame)
        self._parms["validation_frame"] = validation_frame


    @property
    def response_column(self):
        """str: Response variable column."""
        return self._parms.get("response_column")

    @response_column.setter
    def response_column(self, response_column):
        assert_is_type(response_column, None, str)
        self._parms["response_column"] = response_column


    @property
    def ignored_columns(self):
        """List[str]: Names of columns to ignore for training."""
        return self._parms.get("ignored_columns")

    @ignored_columns.setter
    def ignored_columns(self, ignored_columns):
        assert_is_type(ignored_columns, None, [str])
        self._parms["ignored_columns"] = ignored_columns


    @property
    def ignore_const_cols(self):
        """bool: Ignore constant columns. (Default: True)"""
        return self._parms.get("ignore_const_cols")

    @ignore_const_cols.setter
    def ignore_const_cols(self, ignore_const_cols):
        assert_is_type(ignore_const_cols, None, bool)
        self._parms["ignore_const_cols"] = ignore_const_cols


    @property
    def score_each_iteration(self):
        """bool: Whether to score during each iteration of model training. (Default: False)"""
        return self._parms.get("score_each_iteration")

    @score_each_iteration.setter
    def score_each_iteration(self, score_each_iteration):
        assert_is_type(score_each_iteration, None, bool)
        self._parms["score_each_iteration"] = score_each_iteration


    @property
    def balance_classes(self):
        """
        bool: Balance training data class counts via over/under-sampling (for imbalanced data). (Default: False)
        """
        return self._parms.get("balance_classes")

    @balance_classes.setter
    def balance_classes(self, balance_classes):
        assert_is_type(balance_classes, None, bool)
        self._parms["balance_classes"] = balance_classes


    @property
    def class_sampling_factors(self):
        """
        List[float]: Desired over/under-sampling ratios per class (in lexicographic order). If not specified, sampling
        factors will be automatically computed to obtain class balance during training. Requires balance_classes.
        """
        return self._parms.get("class_sampling_factors")

    @class_sampling_factors.setter
    def class_sampling_factors(self, class_sampling_factors):
        assert_is_type(class_sampling_factors, None, [float])
        self._parms["class_sampling_factors"] = class_sampling_factors


    @property
    def max_after_balance_size(self):
        """
        float: Maximum relative size of the training data after balancing class counts (can be less than 1.0). Requires
        balance_classes. (Default: 5)
        """
        return self._parms.get("max_after_balance_size")

    @max_after_balance_size.setter
    def max_after_balance_size(self, max_after_balance_size):
        assert_is_type(max_after_balance_size, None, float)
        self._parms["max_after_balance_size"] = max_after_balance_size


    @property
    def max_confusion_matrix_size(self):
        """
        int: [Deprecated] Maximum size (# classes) for confusion matrices to be printed in the Logs (Default: 20)
        """
        return self._parms.get("max_confusion_matrix_size")

    @max_confusion_matrix_size.setter
    def max_confusion_matrix_size(self, max_confusion_matrix_size):
        assert_is_type(max_confusion_matrix_size, None, int)
        self._parms["max_confusion_matrix_size"] = max_confusion_matrix_size


    @property
    def max_hit_ratio_k(self):
        """
        int: Max. number (top K) of predictions to use for hit ratio computation (for multi-class only, 0 to disable)
        (Default: 0)
        """
        return self._parms.get("max_hit_ratio_k")

    @max_hit_ratio_k.setter
    def max_hit_ratio_k(self, max_hit_ratio_k):
        assert_is_type(max_hit_ratio_k, None, int)
        self._parms["max_hit_ratio_k"] = max_hit_ratio_k


    @property
    def laplace(self):
        """float: Laplace smoothing parameter (Default: 0)"""
        return self._parms.get("laplace")

    @laplace.setter
    def laplace(self, laplace):
        assert_is_type(laplace, None, numeric)
        self._parms["laplace"] = laplace


    @property
    def min_sdev(self):
        """float: Min. standard deviation to use for observations with not enough data (Default: 0.001)"""
        return self._parms.get("min_sdev")

    @min_sdev.setter
    def min_sdev(self, min_sdev):
        assert_is_type(min_sdev, None, numeric)
        self._parms["min_sdev"] = min_sdev


    @property
    def eps_sdev(self):
        """float: Cutoff below which standard deviation is replaced with min_sdev (Default: 0)"""
        return self._parms.get("eps_sdev")

    @eps_sdev.setter
    def eps_sdev(self, eps_sdev):
        assert_is_type(eps_sdev, None, numeric)
        self._parms["eps_sdev"] = eps_sdev


    @property
    def min_prob(self):
        """float: Min. probability to use for observations with not enough data (Default: 0.001)"""
        return self._parms.get("min_prob")

    @min_prob.setter
    def min_prob(self, min_prob):
        assert_is_type(min_prob, None, numeric)
        self._parms["min_prob"] = min_prob


    @property
    def eps_prob(self):
        """float: Cutoff below which probability is replaced with min_prob (Default: 0)"""
        return self._parms.get("eps_prob")

    @eps_prob.setter
    def eps_prob(self, eps_prob):
        assert_is_type(eps_prob, None, numeric)
        self._parms["eps_prob"] = eps_prob


    @property
    def compute_metrics(self):
        """bool: Compute metrics on training data (Default: True)"""
        return self._parms.get("compute_metrics")

    @compute_metrics.setter
    def compute_metrics(self, compute_metrics):
        assert_is_type(compute_metrics, None, bool)
        self._parms["compute_metrics"] = compute_metrics


    @property
    def max_runtime_secs(self):
        """float: Maximum allowed runtime in seconds for model training. Use 0 to disable. (Default: 0)"""
        return self._parms.get("max_runtime_secs")

    @max_runtime_secs.setter
    def max_runtime_secs(self, max_runtime_secs):
        assert_is_type(max_runtime_secs, None, numeric)
        self._parms["max_runtime_secs"] = max_runtime_secs


