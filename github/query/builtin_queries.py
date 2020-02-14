from github.query import Builder


FETCH_ACTOR_AVATAR_URL = """
query fetch_actor_avatar_url ($actor_id: ID!, $size: Int=null) {
  node (id: $actor_id) {
    ... on Actor {
      avatarUrl (size: $size)
    }
  }
}
"""

FETCH_AUTHENTICATED_USER = """
query fetch_authenticated_user {
  viewer {
    __typename
    anyPinnableItems
    avatarUrl
    bio
    company
    createdAt
    databaseId
    id
    isBountyHunter
    isCampusExpert
    isDeveloperProgramMember
    isEmployee
    isHireable
    isSiteAdmin
    isViewer
    location
    login
    name
    pinnedItemsRemaining
    resourcePath
    updatedAt
    url
    websiteUrl
  }
}
"""

FETCH_CODE_OF_CONDUCT = """
query fetch_code_of_conduct ($key: String!) {
  codeOfConduct (key: $key) {
    __typename
    body
    id
    key
    name
    resourcePath
    url
  }
}
"""

FETCH_ALL_CODES_OF_CONDUCT = """
query fetch_all_codes_of_conduct {
  codesOfConduct {
    __typename
    body
    id
    key
    name
    resourcePath
    url
  }
}
"""

FETCH_LICENSE = """
query fetch_license ($key: String!) {
  license (key: $key) {
    __typename
    body
    conditions {
      __typename
      description
      key
      label
    }
    description
    featured
    hidden
    id
    implementation
    key
    limitations {
      __typename
      description
      key
      label
    }
    name
    nickname
    permissions {
      __typename
      description
      key
      label
    }
    pseudoLicense
    spdxId
    url
  }
}
"""

FETCH_ALL_LICENSES = """
query fetch_all_licenses {
  licenses {
    __typename
    body
    conditions {
      __typename
      description
      key
      label
    }
    description
    featured
    hidden
    id
    implementation
    key
    limitations {
      __typename
      description
      key
      label
    }
    name
    nickname
    permissions {
      __typename
      description
      key
      label
    }
    pseudoLicense
    spdxId
    url
  }
}
"""

FETCH_METADATA = """
query fetch_metadata {
  meta {
    __typename
    gitHubServicesSha
    gitIpAddresses
    hookIpAddresses
    importerIpAddresses
    isPasswordAuthenticationVerifiable
    pagesIpAddresses
  }
}
"""

FETCH_NODE = """
query fetch_node ($id: ID!) {
  node (id: $id) {
    __typename
    id
  }
}
"""

FETCH_NODES = """
query fetch_nodes ($ids: [ID!]!) {
  nodes (ids: $ids) {
    __typename
    id
  }
}
"""

FETCH_ORGANIZATION = """
query fetch_organization ($login: String!) {
  organization (login: $login) {
    __typename
    anyPinnableItems
    avatarUrl
    databaseId
    description
    email
    id
    isVerified
    location
    login
    name
    newTeamResourcePath
    newTeamUrl
    pinnedItemsRemaining
    projectsResourcePath
    projectsUrl
    resourcePath
    teamsResourcePath
    teamsUrl
    url
    viewerCanAdminister
    viewerCanChangePinnedItems
    viewerCanCreateProjects
    viewerCanCreateRepositories
    viewerCanCreateTeams
    viewerIsAMember
    websiteUrl
  }
}
"""

FETCH_PROFILEOWNER_EMAIL = """
query fetch_profileowner_email ($profileowner_id: ID!) {
  node (id: $profileowner_id) {
    ... on ProfileOwner {
      email
    }
    ... on Mannequin {
      email
    }
  }
}
"""

FETCH_RATE_LIMIT = """
query fetch_rate_limit {
  rateLimit {
    __typename
    limit
    remaining
    resetAt
  }
}
"""

FETCH_REPOSITORY = """
query fetch_repository ($owner: String!, $name: String!) {
  repository (owner: $owner, name: $name) {
    __typename
    codeOfConduct {
      __typename
      body
      id
      key
      name
      url
    }
    createdAt
    databaseId
    defaultBranchRef {
      name
    }
    description
    diskUsage
    forkCount
    hasIssuesEnabled
    hasWikiEnabled
    id
    isArchived
    isDisabled
    isFork
    isLocked
    isMirror
    isPrivate
    isTemplate
    licenseInfo {
      __typename
      body
      conditions {
        __typename
        description
        key
        label
      }
      description
      featured
      hidden
      id
      implementation
      key
      limitations {
        __typename
        description
        key
        label
      }
      name
      nickname
      permissions {
        __typename
        description
        key
        label
      }
      pseudoLicense
      spdxId
      url
    }
    lockReason
    mergeCommitAllowed
    name
    owner {
      ... on Organization {
        __typename
        anyPinnableItems
        avatarUrl
        databaseId
        description
        email
        id
        isVerified
        location
        login
        name
        newTeamResourcePath
        newTeamUrl
        pinnedItemsRemaining
        projectsResourcePath
        projectsUrl
        resourcePath
        teamsResourcePath
        teamsUrl
        url
        viewerCanAdminister
        viewerCanChangePinnedItems
        viewerCanCreateProjects
        viewerCanCreateRepositories
        viewerCanCreateTeams
        viewerIsAMember
        websiteUrl
      }
      ... on User {
        __typename
        anyPinnableItems
        avatarUrl
        bio
        company
        createdAt
        databaseId
        id
        isBountyHunter
        isCampusExpert
        isDeveloperProgramMember
        isEmployee
        isHireable
        isSiteAdmin
        isViewer
        location
        login
        name
        pinnedItemsRemaining
        resourcePath
        updatedAt
        url
        websiteUrl
      }
    }
    parent {
      __typename
      codeOfConduct {
        __typename
        body
        id
        key
        name
        url
      }
      createdAt
      databaseId
      defaultBranchRef {
        name
      }
      description
      diskUsage
      forkCount
      hasIssuesEnabled
      hasWikiEnabled
      id
      isArchived
      isDisabled
      isFork
      isLocked
      isMirror
      isPrivate
      isTemplate
      licenseInfo {
        __typename
        body
        conditions {
          __typename
          description
          key
          label
        }
        description
        featured
        hidden
        id
        implementation
        key
        limitations {
          __typename
          description
          key
          label
        }
        name
        nickname
        permissions {
          __typename
          description
          key
          label
        }
        pseudoLicense
        spdxId
        url
      }
      lockReason
      mergeCommitAllowed
      name
      owner {
        ... on Organization {
          __typename
          anyPinnableItems
          avatarUrl
          databaseId
          description
          email
          id
          isVerified
          location
          login
          name
          newTeamResourcePath
          newTeamUrl
          pinnedItemsRemaining
          projectsResourcePath
          projectsUrl
          resourcePath
          teamsResourcePath
          teamsUrl
          url
          viewerCanAdminister
          viewerCanChangePinnedItems
          viewerCanCreateProjects
          viewerCanCreateRepositories
          viewerCanCreateTeams
          viewerIsAMember
          websiteUrl
        }
        ... on User {
          __typename
          anyPinnableItems
          avatarUrl
          bio
          company
          createdAt
          databaseId
          id
          isBountyHunter
          isCampusExpert
          isDeveloperProgramMember
          isEmployee
          isHireable
          isSiteAdmin
          isViewer
          location
          login
          name
          pinnedItemsRemaining
          resourcePath
          updatedAt
          url
          websiteUrl
        }
      }
      primaryLanguage {
        __typename
        color
        id
        name
      }
      pushedAt
      rebaseMergeAllowed
      resourcePath
      squashMergeAllowed
      updatedAt
      url
      viewerCanAdminister
      viewerCanCreateProjects
      viewerCanSubscribe
      viewerCanUpdateTopics
      viewerPermission
      viewerSubscription
    }
    primaryLanguage {
      __typename
      color
      id
      name
    }
    pushedAt
    rebaseMergeAllowed
    resourcePath
    squashMergeAllowed
    templateRepository {
      __typename
      codeOfConduct {
        __typename
        body
        id
        key
        name
        url
      }
      createdAt
      databaseId
      defaultBranchRef {
        name
      }
      description
      diskUsage
      forkCount
      hasIssuesEnabled
      hasWikiEnabled
      id
      isArchived
      isDisabled
      isFork
      isLocked
      isMirror
      isPrivate
      isTemplate
      licenseInfo {
        __typename
        body
        conditions {
          __typename
          description
          key
          label
        }
        description
        featured
        hidden
        id
        implementation
        key
        limitations {
          __typename
          description
          key
          label
        }
        name
        nickname
        permissions {
          __typename
          description
          key
          label
        }
        pseudoLicense
        spdxId
        url
      }
      lockReason
      mergeCommitAllowed
      name
      owner {
        ... on Organization {
          __typename
          anyPinnableItems
          avatarUrl
          databaseId
          description
          email
          id
          isVerified
          location
          login
          name
          newTeamResourcePath
          newTeamUrl
          pinnedItemsRemaining
          projectsResourcePath
          projectsUrl
          resourcePath
          teamsResourcePath
          teamsUrl
          url
          viewerCanAdminister
          viewerCanChangePinnedItems
          viewerCanCreateProjects
          viewerCanCreateRepositories
          viewerCanCreateTeams
          viewerIsAMember
          websiteUrl
        }
        ... on User {
          __typename
          anyPinnableItems
          avatarUrl
          bio
          company
          createdAt
          databaseId
          id
          isBountyHunter
          isCampusExpert
          isDeveloperProgramMember
          isEmployee
          isHireable
          isSiteAdmin
          isViewer
          location
          login
          name
          pinnedItemsRemaining
          resourcePath
          updatedAt
          url
          websiteUrl
        }
      }
      primaryLanguage {
        __typename
        color
        id
        name
      }
      pushedAt
      rebaseMergeAllowed
      resourcePath
      squashMergeAllowed
      updatedAt
      url
      viewerCanAdminister
      viewerCanCreateProjects
      viewerCanSubscribe
      viewerCanUpdateTopics
      viewerPermission
      viewerSubscription
    }
    updatedAt
    url
    viewerCanAdminister
    viewerCanCreateProjects
    viewerCanSubscribe
    viewerCanUpdateTopics
    viewerPermission
    viewerSubscription
  }
}
"""

FETCH_REPOSITORY_ASSIGNABLE_USERS = """
query fetch_repository_assignable_users ($repository_id: ID!, $cursor: String!) {
  node (id: $repository_id) {
    ... on Repository {
      assignableUsers (first: 10, after: $cursor) {
        nodes {
          __typename
          anyPinnableItems
          avatarUrl
          bio
          company
          createdAt
          databaseId
          id
          isBountyHunter
          isCampusExpert
          isDeveloperProgramMember
          isEmployee
          isHireable
          isSiteAdmin
          isViewer
          location
          login
          name
          pinnedItemsRemaining
          resourcePath
          updatedAt
          url
          websiteUrl
        }
        pageInfo {
          endCursor
          hasNextPage
        }
      }
    }
  }
}
"""

FETCH_REPOSITORY_COLLABORATORS = """
query fetch_repository_collaborators ($repository_id: ID!, $cursor: String!) {
  node (id: $repository_id) {
    ... on Repository {
      collaborators (first: 10, after: $cursor) {
        nodes {
          __typename
          anyPinnableItems
          avatarUrl
          bio
          company
          createdAt
          databaseId
          id
          isBountyHunter
          isCampusExpert
          isDeveloperProgramMember
          isEmployee
          isHireable
          isSiteAdmin
          isViewer
          location
          login
          name
          pinnedItemsRemaining
          resourcePath
          updatedAt
          url
          websiteUrl
        }
        pageInfo {
          endCursor
          hasNextPage
        }
      }
    }
  }
}
"""

FETCH_TOPIC = """
query fetch_topic ($name: String!) {
  topic (name: $name) {
    __typename
    id
    name
    relatedTopics (first: 10) {
      __typename
      id
      name
    }
  }
}
"""

FETCH_USER = """
query fetch_user ($login: String!) {
  user (login: $login) {
    __typename
    anyPinnableItems
    avatarUrl
    bio
    company
    createdAt
    databaseId
    id
    isBountyHunter
    isCampusExpert
    isDeveloperProgramMember
    isEmployee
    isHireable
    isSiteAdmin
    isViewer
    location
    login
    name
    pinnedItemsRemaining
    resourcePath
    updatedAt
    url
    websiteUrl
  }
}
"""

FETCH_USER_COMMIT_COMMENTS = """

"""



FETCH_REPO_INFO= """
query fetch_repository_info ($owner: String!, $name: String!) {
  repository (owner: $owner, name: $name) {
    databaseId
    name
    owner{
      login
    }
    createdAt
    pushedAt
    primaryLanguage{
      name
    }
    languages{
      totalCount
    }
    
    commitComments{
      totalCount
    }
    
    forkCount
    isArchived
    isFork
    isLocked
    isMirror
    stargazers{
      totalCount
    }
    watchers{
      totalCount
    }
    
    labels{
      totalCount
    }
    
    issues(last:100)
    {
      totalCount
      pageInfo{
        	startCursor
      		endCursor
      }
      edges{
        cursor
        node{
          id
          author{
            login
          }
          body
          number
          title
          createdAt
          participants{
            totalCount
          }
          state
          closedAt
          comments(first:100)
          {
            totalCount
            pageInfo{
                startCursor
                endCursor
            }
            edges{
              cursor
              node{
                author{
                  login
                }
                body
                createdAt
              }
            }
          }
        }
      }
    }
    pullRequests(last:100)
    {
      totalCount
      pageInfo{
        	startCursor
      		endCursor
      }
      edges{
        cursor
        node{
          id
          author{
            login
          }
          body
          number
          title
          createdAt
          participants{
            totalCount
          }
          state
          closedAt
          comments(first:100)
          {
            totalCount
            pageInfo{
                startCursor
                endCursor
            }
            edges{
              cursor
              node{
                author{
                  login
                }
                body
                createdAt
              }
            }
          }
        }
      }
    }
  }
  rateLimit {
    limit
    cost
    remaining
    resetAt
  }
}
"""